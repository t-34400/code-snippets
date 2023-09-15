#nullable enable

using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

namespace MovementHistory.Viewer.IO
{
    class ToggleGroupManager : MonoBehaviour
    {
        private const string TEXT_CHILD_NAME = "Text (TMP)";

        [SerializeField] private GameObject togglePrefab = default!;
        [SerializeField] private GameObject toggleRootObject = default!;
        [SerializeField] private ScrollRect scrollRect = default!;
        [SerializeField] private ToggleGroup toggleGroup = default!;

        private readonly List<(Toggle toggle, TMP_Text labelUpdater)> togglePool = new();
        private readonly List<(Toggle toggle, string toggleLabel)> currentToggleLabels = new();

        internal IReadOnlyList<(Toggle toggle, string toggleLabel)> CurrentDirectories => currentToggleLabels;

        internal void UpdateToggles(List<string> toggleLabels)
        {
            currentToggleLabels.Clear();
            togglePool.ForEach(pair => pair.toggle.gameObject.SetActive(false));

            while(togglePool.Count < toggleLabels.Count)
            {
                var toggleObject = Instantiate(togglePrefab);

                toggleObject.transform.SetParent(toggleRootObject.transform);
                toggleObject.transform.localScale = Vector3.one;
                toggleObject.transform.localPosition = Vector3.zero;
                toggleObject.transform.localRotation = Quaternion.identity;

                var toggle = toggleObject.GetComponent<Toggle>();
                var textObject = toggleObject.transform.Find(TEXT_CHILD_NAME);
                var tmp_text = textObject?.GetComponent<TMP_Text>();

                if(toggle == null || tmp_text == null)
                {
                    Debug.LogError("Failed to retrieve Toggle or LabelUpdater component from directory toggle prefab.");
                    Destroy(toggleObject);
                    return;
                }

                togglePool.Add((toggle, tmp_text));
            }

            foreach(var (toggleName, index) in toggleLabels.Select((item, index) => (item, index)))
            {
                var (toggle, tmp_text) = togglePool[index];
                
                tmp_text.text = toggleName;

                toggle.group = toggleGroup;
                toggle.gameObject.SetActive(true);

                currentToggleLabels.Add((toggle, toggleName));
            }

            scrollRect.verticalNormalizedPosition = 0;
        }

        internal bool TryGetCurrentSelectedLabel(out string label)
        {
            label = "";
            var selected = currentToggleLabels.Where(pair => pair.toggle.isOn);
            if(selected.Count() > 0)
            {
                label = selected.First().toggleLabel;
                return true;
            }

            return false;
        }
    }
}
