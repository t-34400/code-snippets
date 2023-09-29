#nullable enable

using System;
using UnityEngine;

using Oculus.Interaction.HandGrab;

namespace OculusHelpers
{
    class HandleGrabHandedEvent : HandleGrabEvent, IHandleGrabHandedEvent
    {
        [SerializeField] private HandGrabInteractorManager handGrabInteractorManager = default!;

        private event Action<Handed>? HandedGrabbed;
        private event Action<Handed>? HandedReleased;

        event Action<Handed> IHandleGrabHandedEvent.Grabbed
        {
            add { HandedGrabbed += value; }
            remove { HandedGrabbed -= value; }
        }

        event Action<Handed> IHandleGrabHandedEvent.Released
        {
            add { HandedReleased += value; }
            remove { HandedReleased -= value; }
        }

        private new void Start()
        {
            base.Start();

            HandGrabInteractable.WhenSelectingInteractorAdded.Action += WhenInteractorAdded;
            HandGrabInteractable.WhenSelectingInteractorRemoved.Action += WhenSelectingInteractorRemoved;
        }

        private new void OnDestroy()
        {
            if(HandGrabInteractable != null)
            {
                HandGrabInteractable.WhenSelectingInteractorAdded.Action -= WhenInteractorAdded;
                HandGrabInteractable.WhenSelectingInteractorRemoved.Action -= WhenSelectingInteractorRemoved;
            }
        }

        private void WhenInteractorAdded(HandGrabInteractor handGrabInteractor)
        {
            if(handGrabInteractorManager.TryGetGrabHand(handGrabInteractor, out var handed))
            {
                HandedGrabbed?.Invoke(handed);
            }
        }

        private void WhenSelectingInteractorRemoved(HandGrabInteractor handGrabInteractor)
        {
            if(handGrabInteractorManager.TryGetGrabHand(handGrabInteractor, out var handed))
            {
                HandedReleased?.Invoke(handed);
            }
        }
    }
}