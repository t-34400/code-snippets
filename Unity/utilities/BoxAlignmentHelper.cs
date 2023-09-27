#nullable enable

using UnityEngine;

namespace UnityUtility
{
    public static class BoxAlignmentHelper
    {
        public static BoxBottomFace GetBoxBottomFace(Quaternion objectRotation, out Quaternion downwardRotation)
        {
            var localRightVector = objectRotation * Vector3.right;
            var localUpVector = objectRotation * Vector3.up;
            var localForwardVector = objectRotation * Vector3.forward;

            var rightComponent = Vector3.Dot(Vector3.down, localRightVector);
            var upComponent = Vector3.Dot(Vector3.down, localUpVector);
            var forwardComponent = Vector3.Dot(Vector3.down, localForwardVector);

            var absRightComponent = Mathf.Abs(rightComponent);
            var absUpComponent = Mathf.Abs(upComponent);
            var absForwardComponent = Mathf.Abs(forwardComponent);

            if(absUpComponent >= absRightComponent && absUpComponent >= absForwardComponent)
            {
                if(upComponent > 0)
                {
                    downwardRotation = Quaternion.FromToRotation(localUpVector, Vector3.down);
                    return BoxBottomFace.Top;
                }
                else
                {
                    downwardRotation = Quaternion.FromToRotation(-localUpVector, Vector3.down);
                    return BoxBottomFace.Bottom;
                }
            }
            else if(absRightComponent >= absUpComponent && absRightComponent >= absForwardComponent)
            {
                if(rightComponent > 0)
                {
                    downwardRotation = Quaternion.FromToRotation(localRightVector, Vector3.down);
                    return BoxBottomFace.Right;
                }
                else
                {
                    downwardRotation = Quaternion.FromToRotation(-localRightVector, Vector3.down);
                    return BoxBottomFace.Left;
                }
            }
            else
            {
                if(forwardComponent > 0)
                {
                    downwardRotation = Quaternion.FromToRotation(localForwardVector, Vector3.down);
                    return BoxBottomFace.Front;
                }
                else
                {
                    downwardRotation = Quaternion.FromToRotation(-localForwardVector, Vector3.down);
                    return BoxBottomFace.Back;
                }
            }
        }

        public static (Vector3 width, Vector3 depth) GetAlignedWidthAndDepthVector(Quaternion objectRotation)
        {
            var localRightVector = objectRotation * Vector3.right;
            var localUpVector = objectRotation * Vector3.up;
            var localForwardVector = objectRotation * Vector3.forward;

            var (down, width, depth) = GetDownWidthDepthVectors(localRightVector, localUpVector, localForwardVector);
            var downwardRotation = Quaternion.FromToRotation(down, Vector3.down);
            width = downwardRotation * width;
            depth = downwardRotation * depth;

            return (width, depth);
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

        private static Vector3 GetDownwardFaceVector(Vector3 localRightVector, Vector3 localUpVector, Vector3 localForwardVector)
        {
            var rightComponent = Vector3.Dot(Vector3.down, localRightVector);
            var upComponent = Vector3.Dot(Vector3.down, localUpVector);
            var forwardComponent = Vector3.Dot(Vector3.down, localForwardVector);

            var absRightComponent = Mathf.Abs(rightComponent);
            var absUpComponent = Mathf.Abs(upComponent);
            var absForwardComponent = Mathf.Abs(forwardComponent);

            if(absUpComponent >= absRightComponent && absUpComponent >= absForwardComponent)
            {
                return (upComponent > 0) ? localUpVector : -localUpVector;
            }
            else if(absRightComponent >= absUpComponent && absRightComponent >= absForwardComponent)
            {
                return (rightComponent > 0) ? localRightVector : -localRightVector;
            }
            else
            {
                return (forwardComponent > 0) ? localForwardVector : -localForwardVector;
            }
        }

        public enum BoxBottomFace
        {
            Front,
            Back,
            Left,
            Right,
            Top,
            Bottom
        }
    }
}
