#nullable enable
using System.Collections.Generic;
using UnityEngine;

class CollisionIgnoreController : MonoBehaviour
{
    [SerializeField] private List<Collider> ignoredColliders = new List<Collider>();

    private void Awake()
    {
        for (int i = 0; i < ignoredColliders.Count; i++)
        {
            for (int j = i + 1; j < ignoredColliders.Count; j++)
            {
                Physics.IgnoreCollision(ignoredColliders[i], ignoredColliders[j]);
            }
        }
    }
}
