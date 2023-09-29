#nullable enable

using UnityEngine;
using Oculus.Interaction.HandGrab;

namespace OculusHelpers
{
    [CreateAssetMenu(fileName = "HandGrabInteractorManager", menuName = "Oculus Helpers/Data/Hand Grab Interactor Manager")]
    public class HandGrabInteractorManager : ScriptableObject
    {
        [SerializeField] private HandGrabInteractor? leftHandGrabInteractor = null;
        [SerializeField] private HandGrabInteractor? rightHandGrabInteractor = null;

        internal void SetInteractors(HandGrabInteractor? leftHandGrabInteractor, HandGrabInteractor? rightHandGrabInteractor)
        {
            this.leftHandGrabInteractor = leftHandGrabInteractor;
            this.rightHandGrabInteractor = rightHandGrabInteractor;
        }

        public bool TryGetGrabHand(HandGrabInteractor handGrabInteractor, out Handed handed)
        {
            handed = default!;

            if(leftHandGrabInteractor != null && handGrabInteractor == leftHandGrabInteractor)
            {
                handed = Handed.Left;
                return true;
            }

            if(rightHandGrabInteractor != null && handGrabInteractor == rightHandGrabInteractor)
            {
                handed = Handed.Right;
                return true;
            }

            return false;
        }
    }
}