#nullable enable

using System;

namespace OculusHelpers
{
    class MockHandleGrabEvent : HandleGrabEventBase
    {
        private event Action? Selected;
        private event Action? Unselected;

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

        private void Start()
        {
            enabled = false;
        }

        private void OnEnable()
        {
            Selected?.Invoke();
        }

        private void OnDisable()
        {
            Unselected?.Invoke();
        }
    }
}
