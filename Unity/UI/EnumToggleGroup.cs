#nullable enable

using System;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using UnityEngine.Events;
using UnityEngine.UI;

namespace UnityHelper
{
    [Serializable]
    public class EnumToggleGroup<T> where T : Enum
    {
        [SerializeField] private List<EnumToggle<T>> enumToggles = default!;

        private event Action<T>? onValueChanged;
        public event Action<T>? OnValueChanged
        {
            add 
            { 
                if(onValueChanged == null)
                {
                    enumToggles.ForEach(toggle => toggle.OnValueChanged += OnToggleValueChanged);
                }
                onValueChanged += value; 
            }
            remove
            {
                onValueChanged -= value;
                if(onValueChanged == null)
                {
                    enumToggles.ForEach(toggle => toggle.OnValueChanged -= OnToggleValueChanged);
                }
            }
        }

        public bool TryGetValue(out T value)
        {
            var index = enumToggles.FindIndex(toggle => toggle.IsOn);
            value = enumToggles.ElementAtOrDefault(index).Value;
            return index > -1;
        }

        public void SetValue(T value)
        {
            var index = enumToggles.FindIndex(toggle => Equals(toggle.Value, value));
            if(index > -1)
            {
                enumToggles.ElementAt(index).IsOn = true;
            }
        }

        public void SetInteractableState(T value, bool interactable)
        {
            var index = enumToggles.FindIndex(toggle => Equals(toggle.Value, value));
            if(index > -1)
            {
                enumToggles.ElementAt(index).Interactable = interactable;
            }
        }

        private void OnToggleValueChanged(T enumValue, bool value)
        {
            if(value == true)
            {
                onValueChanged?.Invoke(enumValue);
            }
        }
    }

    [Serializable]
    class EnumToggle<T> where T : Enum
    {
        [SerializeField] private T enumValue = default!;
        [SerializeField] private Toggle toggle = default!;

        private Dictionary<Action<T, bool>, UnityAction<bool>> unityActionMap = new();

        internal T Value => enumValue;
        internal bool IsOn
        {
            get => toggle.isOn;
            set => toggle.isOn = value;
        }
        internal bool Interactable
        {
            get => toggle.interactable;
            set => toggle.interactable = value;
        }

        internal event Action<T, bool> OnValueChanged
        {
            add 
            {
                if(toggle != null)
                {
                    var unityAction = new UnityAction<bool>(isOn => value.Invoke(Value, isOn));
                    toggle.onValueChanged.AddListener(unityAction);
                    unityActionMap[value] = unityAction; 
                }
            }
            remove
            {
                if(unityActionMap.TryGetValue(value, out var unityAction))
                {
                    if(toggle != null)
                    {
                        toggle.onValueChanged.RemoveListener(unityAction);
                    }
                    unityActionMap.Remove(value);
                }
            }
        }
    }
}
