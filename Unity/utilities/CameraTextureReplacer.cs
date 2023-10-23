#nullable enable

using System.Collections.Generic;
using System.Linq;
using UnityEngine;

namespace Utility
{
    class CameraTextureReplacer : MonoBehaviour
    {
        [SerializeField] private Renderer targetRenderer = default!;
        [SerializeField] private List<int> targetMaterialIndices = default!;

        [SerializeField] private Camera textureCamera = default!;
        [SerializeField] private Vector2 captureSize = default!;
        [SerializeField] private Vector2Int textureSize = default!;

        public void Generate()
        {
            var texture = GenerateTexture();
            ApplyTexture(texture);
        }

        private void ApplyTexture(Texture2D texture)
        {
            var materialCount = targetRenderer.materials.Count();

            foreach(var index in targetMaterialIndices)
            {
                if(index < materialCount)
                {
                    var material = targetRenderer.materials[index];
                    material.mainTexture = texture;
                }
            }
        }

        private Texture2D GenerateTexture()
        {
            var renderTexture = new RenderTexture(textureSize.x, textureSize.y, 24);
            textureCamera.targetTexture = renderTexture;

            textureCamera.orthographic = true;
            textureCamera.orthographicSize = captureSize.y / 2;
            textureCamera.aspect = captureSize.x / captureSize.y;
            textureCamera.Render();

            var capturedTexture = new Texture2D(renderTexture.width, renderTexture.height);

            RenderTexture.active = renderTexture;
            capturedTexture.ReadPixels(new Rect(0, 0, renderTexture.width, renderTexture.height), 0, 0);
            capturedTexture.Apply();
            RenderTexture.active = null;

            textureCamera.targetTexture = null;
            Destroy(renderTexture);

            return capturedTexture;            
        }
    }
}
