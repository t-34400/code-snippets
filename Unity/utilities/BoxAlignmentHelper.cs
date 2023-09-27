#nullable enable

using UnityEngine;

public static class BoxAlignmentHelper
{
    public Quaternion GetTargetWorldRotation()
    {
        var handleRotation = boxObject.rotation;

        var rightVector = boxObject.right;
        var upVector = boxObject.up;
        var forwardVector = boxObject.forward;

        var downwardFaceVector = GetDownwardFaceVector(rightVector, upVector, forwardVector);
        return Quaternion.FromToRotation(downwardFaceVector, Vector3.down) * handleRotation;
    }

    private static Vector3 GetDownwardFaceVector(Vector3 rightVector, Vector3 upVector, Vector3 forwardVector)
    {
        var rightComponent = Vector3.Dot(Vector3.down, rightVector);
        var upComponent = Vector3.Dot(Vector3.down, upVector);
        var forwardComponent = Vector3.Dot(Vector3.down, forwardVector);

        var absRightComponent = Mathf.Abs(rightComponent);
        var absUpComponent = Mathf.Abs(upComponent);
        var absForwardComponent = Mathf.Abs(forwardComponent);

        if(absUpComponent >= absRightComponent && absUpComponent >= absForwardComponent)
        {
            return (upComponent > 0) ? upVector : -upVector;
        }
        else if(absRightComponent >= absUpComponent && absRightComponent >= absForwardComponent)
        {
            return (rightComponent > 0) ? rightVector : -rightVector;
        }
        else
        {
            return (forwardComponent > 0) ? forwardVector : -forwardVector;
        }
    }
}
