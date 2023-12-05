using UnityEngine;

public static class VectorQuaternionUtils
{
    public static Quaternion GetMirroredRotation(Quaternion rotation, Quaternion defaultRotation, Vector3 mirrorNormal)
    {
        var inverseDefaultRotation = Quaternion.Inverse(defaultRotation);
        
        var localRotation = inverseDefaultRotation * rotation;
        var localMirrorNormal = inverseDefaultRotation * mirrorNormal;

        localRotation.ToAngleAxis(out var angle, out var axis);

        var mirroredAxis = GetMirroredVector(axis, localMirrorNormal);

        return defaultRotation * Quaternion.AngleAxis(-angle, mirroredAxis);
    }

    public static Vector3 GetMirroredVector(Vector3 sourceVector, Vector3 mirrorNormal)
    {
        var projection = Vector3.Project(sourceVector, mirrorNormal);
        return sourceVector - 2 * projection;
    }
}
