#nullable enable

using UnityEngine;

public class TransformExtension
{
    public static bool TryGetChild(this Transform parent, string name, out Transform result)
    {
        foreach (Transform child in parent)
        {
            if (child.name == name)
            {
                result = child;
                return true;
            }

            if (child.childCount > 0)
            {
                if (TryGetChild(child, name, out result))
                {
                    return true;
                }
            }
        }

        result = default!;
        return false;
    }
}
