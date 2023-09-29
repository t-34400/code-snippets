#nullable enable

using System;

namespace OculusHelpers
{
    public interface IHandleGrabEvent
    {
        event Action? Grabbed;
        event Action? Released;
    }
}