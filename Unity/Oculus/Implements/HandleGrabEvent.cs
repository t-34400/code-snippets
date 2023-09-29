#nullable enable

using System;
using UnityEngine;
using Oculus.Interaction;
using Oculus.Interaction.HandGrab;

namespace OculusHelpers
{
    public abstract class HandleGrabEventBase : MonoBehaviour, IHandleGrabEvent
    {
        public abstract event Action? Grabbed;
        public abstract event Action? Released;
    }

    class HandleGrabEvent : HandleGrabEventBase
    {
        [SerializeField] private HandGrabInteractable handGrabInteractable = default!;

        private event Action? Selected;
        private event Action? Unselected;

        protected HandGrabInteractable HandGrabInteractable => handGrabInteractable;

        public override event Action? Grabbed
        {
            add { Selected += value; }
            remove { Selected -= value; }
        }

        public override event Action? Released
        {
            add { Unselected += value; }
            remove { Unselected -= value; }
        }

        protected void Start()
        {
            handGrabInteractable.WhenStateChanged += HandleStateChanged;
        }

        protected void OnDestroy()
        {
            if(handGrabInteractable != null)
            {
                handGrabInteractable.WhenStateChanged -= HandleStateChanged;
            }
        }

        private void HandleStateChanged(InteractableStateChangeArgs args)
        {
            switch (args.NewState)
            {
                case InteractableState.Hover:
                    if (args.PreviousState == InteractableState.Select)
                    {
                        Unselected?.Invoke();
                    }

                    break;
                case InteractableState.Select:
                    if (args.PreviousState == InteractableState.Hover)
                    {
                        Selected?.Invoke();
                    }

                    break;
            }
        }
    }
}