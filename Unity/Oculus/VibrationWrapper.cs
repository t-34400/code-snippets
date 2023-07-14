#nullable enable
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;

internal class VibrationSettings
{
    private float _frequency;
    private float _amplitude;

    internal VibrationSettings(float frequency = 1.0f, float amplitude = 1.0f)
    {
        this._frequency = frequency;
        this._amplitude = amplitude;
    }

    internal float frequency => _frequency;
    internal float amplitude => _amplitude;
}

class VibrationWrapper : MonoBehaviour
{
    // Controller vibration automatically ends two seconds after the last input,
    // so the next input must be entered periodically.
    private const float INPUT_INTERVAL_SEC = 1.0f;

    private readonly List<VibrationSettings> leftHandVibrationSettingsList = new List<VibrationSettings>();
    private readonly List<VibrationSettings> rightHandVibrationSettingsList = new List<VibrationSettings>();

    private bool isLeftHandCoroutineRunning = false;
    private bool isRightHandCoroutineRunning = false;

    public void StartLeftHandVibration(VibrationSettings vibrationSettings, float? duration = null)
    {
        leftHandVibrationSettingsList.Add(vibrationSettings);

        if(!isLeftHandCoroutineRunning)
        {
            isLeftHandCoroutineRunning = true;
            StartCoroutine(Vibrate(OVRInput.Controller.LHand));
        }
    }

    public void StartRightHandVibration(VibrationSettings vibrationSettings, float? duration = null)
    {
        rightHandVibrationSettingsList.Add(vibrationSettings);

        if(!isRightHandCoroutineRunning)
        {
            isRightHandCoroutineRunning = true;
            StartCoroutine(Vibrate(OVRInput.Controller.RHand));
        }
    }

    public void EndLeftHandVibration(VibrationSettings vibrationSettings)
    {
        leftHandVibrationSettingsList.Remove(vibrationSettings);
    }

    public void EndRightHandVibration(VibrationSettings vibrationSettings)
    {
        rightHandVibrationSettingsList.Remove(vibrationSettings);
    }

    private IEnumerator Vibrate(OVRInput.Controller controller)
    {
        var vibrationSettingsList = GetVibrationSettingsList(controller);
        if(vibrationSettingsList == null)
        {
            yield break;
        }

        var previousInputTime = 0.0f;
        VibrationSettings? previousVibrationSettings = null;
        
        while(vibrationSettingsList.Count > 0)
        {
            var currentTime = Time.time;
            var currentVibrationSettings = vibrationSettingsList.Last();
            
            if(currentVibrationSettings == previousVibrationSettings && currentTime - previousInputTime < INPUT_INTERVAL_SEC)
            {
                yield return null;
            }

            previousInputTime = currentTime;
            OVRInput.SetControllerVibration(currentVibrationSettings.frequency, currentVibrationSettings.amplitude, controller);
            yield return null;
        }

        OVRInput.SetControllerVibration(0.0f, 0.0f, controller);
        SetCoroutineRunningStateFalse(controller);
    }

    private List<VibrationSettings>? GetVibrationSettingsList(OVRInput.Controller controller)
    {
        switch(controller)
        {
            case OVRInput.Controller.LTouch:
                {
                    return leftHandVibrationSettingsList;
                }
            case OVRInput.Controller.RTouch:
                {
                    return rightHandVibrationSettingsList;
                }
            default:
                {
                    return null;
                }
        }
    }

    private IEnumerator StopVibrationAfterDelay(OVRInput.Controller controller, VibrationSettings vibrationSettings, float delay)
    {
        yield return new WaitForSeconds(delay);

        GetVibrationSettingsList(controller)?.Remove(vibrationSettings);
    }

    private void SetCoroutineRunningStateFalse(OVRInput.Controller controller)
    {
        switch(controller)
        {
            case OVRInput.Controller.LTouch:
                {
                    isLeftHandCoroutineRunning = false;
                    return;
                }
            case OVRInput.Controller.RTouch:
                {
                    isRightHandCoroutineRunning = false;
                    return;
                }
        }
    }
}
