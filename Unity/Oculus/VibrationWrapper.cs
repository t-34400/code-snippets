#nullable enable

using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

using UnityEngine;

namespace OculusHelpers
{
    record VibrationSettings(float frequency = 1.0f, float amplitude = 1.0f);

    class VibrationWrapper : MonoBehaviour
    {
        // Controller vibration automatically ends two seconds after the last input,
        // so the next input must be entered periodically.
        private const float INPUT_INTERVAL_SEC = 1.0f;

        private readonly List<(Guid vibrationId, VibrationSettings settings)> leftHandVibrationSettingsList = new();
        private readonly List<(Guid vibrationId, VibrationSettings settings)> rightHandVibrationSettingsList = new();

        private bool isLeftHandCoroutineRunning = false;
        private bool isRightHandCoroutineRunning = false;

        public Guid StartLeftHandVibration(VibrationSettings vibrationSettings)
        {
            var vibrationId = Guid.NewGuid();
            leftHandVibrationSettingsList.Add((vibrationId, vibrationSettings));

            if(!isLeftHandCoroutineRunning)
            {
                isLeftHandCoroutineRunning = true;
                StartCoroutine(Vibrate(OVRInput.Controller.LTouch));
            }

            return vibrationId;
        }

        public Guid StartRightHandVibration(VibrationSettings vibrationSettings)
        {
            var vibrationId = Guid.NewGuid();
            rightHandVibrationSettingsList.Add((vibrationId, vibrationSettings));

            if(!isRightHandCoroutineRunning)
            {
                isRightHandCoroutineRunning = true;
                StartCoroutine(Vibrate(OVRInput.Controller.RTouch));
            }

            return vibrationId;
        }

        public void StopLeftHandVibration(Guid vibrationId)
        {
            Debug.Log($"Before stop left: {leftHandVibrationSettingsList.Count}");
            var message = "Before stop left ids:\n";
            foreach(var setting in leftHandVibrationSettingsList)
            {
                message += $"{setting.vibrationId}\n";
            }
            Debug.Log(message);
            leftHandVibrationSettingsList.RemoveAll(pair => pair.vibrationId == vibrationId);
            Debug.Log($"After stop left: {leftHandVibrationSettingsList.Count}");
        }

        public void StopRightHandVibration(Guid vibrationId)
        {
            rightHandVibrationSettingsList.RemoveAll(pair => pair.vibrationId == vibrationId);
        }

        private IEnumerator Vibrate(OVRInput.Controller controller)
        {
            var vibrationSettingsList = GetVibrationSettingsList(controller);
            if(vibrationSettingsList == null)
            {
                yield break;
            }

            var previousInputTime = 0.0f;
            Guid? previousVibrationId = null;
            
            while(vibrationSettingsList.Count > 0)
            {
                var currentTime = Time.time;
                var currentPair = vibrationSettingsList.Last();
                
                if(currentPair.vibrationId == previousVibrationId && currentTime - previousInputTime < INPUT_INTERVAL_SEC)
                {
                    yield return null;
                }

                previousInputTime = currentTime;
                previousVibrationId = currentPair.vibrationId;
                OVRInput.SetControllerVibration(currentPair.settings.frequency, currentPair.settings.amplitude, controller);
                yield return null;
            }

            OVRInput.SetControllerVibration(0.0f, 0.0f, controller);
            SetCoroutineRunningStateFalse(controller);
        }

        private List<(Guid vibrationId, VibrationSettings settings)>? GetVibrationSettingsList(OVRInput.Controller controller)
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
}
