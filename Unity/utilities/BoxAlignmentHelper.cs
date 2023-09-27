#nullable enable

using UnityEngine;

public static class BoxAlignmentHelper
{
    public static Quaternion GetTargetWorldRotation(Quaternion objectRotation)
    {
        var localRightVector = objectRotation * Vector3.right;
        var localUpVector = objectRotation * Vector3.up;
        var localForwardVector = objectRotation * Vector3.forward;

        var downwardFaceVector = GetDownwardFaceVector(localRightVector, localUpVector, localForwardVector);
        return Quaternion.FromToRotation(downwardFaceVector, Vector3.down) * objectRotation;
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

    private static (Vector3 down, Vector3 width, Vector3 depth) GetDownWidthDepthVectors(Vector3 localRightVector, Vector3 localUpVector, Vector3 localForwardVector)
    {
        var rightComponent = Vector3.Dot(Vector3.down, localRightVector);
        var upComponent = Vector3.Dot(Vector3.down, localUpVector);
        var forwardComponent = Vector3.Dot(Vector3.down, localForwardVector);

        var absRightComponent = Mathf.Abs(rightComponent);
        var absUpComponent = Mathf.Abs(upComponent);
        var absForwardComponent = Mathf.Abs(forwardComponent);

        if(absUpComponent >= absRightComponent && absUpComponent >= absForwardComponent)
        {
            return (upComponent > 0) ? (localUpVector, -localRightVector, localForwardVector) : (-localUpVector, localRightVector, -localForwardVector);
        }
        else if(absRightComponent >= absUpComponent && absRightComponent >= absForwardComponent)
        {
            return (rightComponent > 0) ? (localRightVector, localForwardVector, -localUpVector) : (-localRightVector, -localForwardVector, localUpVector);
        }
        else
        {
            return (forwardComponent > 0) ? (localForwardVector, localUpVector, -localRightVector) : (-localForwardVector, -localUpVector, localRightVector);
        }
    }
}
