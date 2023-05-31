using UnityEngine;
using UnityEngine.UI;

public class WebCamDisplayController : MonoBehaviour
{
    [SerializeField]
    private RawImage rawImage;

    private WebCamTexture webCamTexture = null;

    void Start()
    {
        if(WebCamTexture.devices.Length == 0)
        {
            Debug.Log("No webcam device found.");
            return;
        }
        webCamTexture = new WebCamTexture();
        rawImage.texture = webCamTexture;

        webCamTexture.Play();
        
        if(!webCamTexture.isPlaying)
        {
            Debug.Log("Failed to start WebCamTexture.");
            return;
        }

        AdjustRawImageSize();
    }

    void OnDestroy()
    {
        webCamTexture.Stop();
    }

    private void AdjustRawImageSize()
    {
        var aspectRatio = (float) webCamTexture.width / webCamTexture.height;

        var rectTransform = rawImage.GetComponent<RectTransform>();
        rectTransform.sizeDelta = new Vector2(aspectRatio * UIConstants.WEB_CAM_DISPLAY_HEIGHT, UIConstants.WEB_CAM_DISPLAY_HEIGHT);
    }
}
