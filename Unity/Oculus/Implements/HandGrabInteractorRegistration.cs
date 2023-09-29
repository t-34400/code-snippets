#nullable enable

using System;
using UnityEngine;
using Oculus.Interaction;
using Oculus.Interaction.HandGrab;

namespace OculusHelpers
{
    public class HandGrabInteractorRegistration : MonoBehaviour
    {
        [SerializeField] private HandGrabInteractor leftHandGrabInteractor = default!;
        [SerializeField] private HandGrabInteractor rightHandGrabInteractor = default!;

        [SerializeField] private HandGrabInteractorManager handGrabInteractorManager = default!;

        private void Start()
        {
            handGrabInteractorManager.SetInteractors(leftHandGrabInteractor, rightHandGrabInteractor);
        }

        private void OnDestroy()
        {
            handGrabInteractorManager.SetInteractors(null, null);
        }
    }
}