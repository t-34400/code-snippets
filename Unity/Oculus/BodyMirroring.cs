using System.Collections;
using System.Collections.Generic;
using System.Linq;
using Oculus.Interaction.Body.Input;
using UnityEngine;

public class BodyMirroring : MonoBehaviour
{
    public OVRCustomSkeleton sourceSkeleton;
    public OVRCustomSkeleton targetSkeleton;

    public GameObject anchor;

    private Quaternion defaultRotation = Quaternion.Euler(0, -90, -90);

    public HashSet<int> list = new();

    void Start()
    {
        foreach(var id in System.Enum.GetValues(typeof(BodyJointId)).Cast<BodyJointId>())
        {
            if (!id.ToString().Contains("Left") && !id.ToString().Contains("Right"))
            {
                var index = (int) id;
                Debug.Log($"{index} {sourceSkeleton.CustomBones.Count}");
                if(index >= 0 && index < sourceSkeleton.CustomBones.Count)
                {
                    Debug.Log(id.ToString());
                    list.Add(index);
                }
            }
        }
    }

    // Update is called once per frame
    void Update()
    {
        var mirrorAxis = anchor.transform.right;
        var anchorPosition = anchor.transform.position;

        foreach (var index in list)
        {
            var targetTransform = targetSkeleton.CustomBones.ElementAt(index);
            var sourceTransform = sourceSkeleton.CustomBones.ElementAt(index);

            if(targetTransform == null || sourceTransform == null)
            {
                continue;
            }

            var position = sourceTransform.position;
            var rotation = sourceTransform.rotation;

            var positionDelta = position - anchorPosition;

            var targetPosition = anchorPosition + VectorQuaternionUtils.GetMirroredVector(positionDelta, mirrorAxis);
            var targetRotation = VectorQuaternionUtils.GetMirroredRotation(rotation, defaultRotation, mirrorAxis);

            targetTransform.SetPositionAndRotation(targetPosition, targetRotation);
        }
    }
}
