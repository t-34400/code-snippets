#nullable enable

using System;

namespace OculusHelpers
{
    public interface IHandleGrabHandedEvent
    {
        event Action<Handed> Grabbed;
        event Action<Handed> Released;
    }
}