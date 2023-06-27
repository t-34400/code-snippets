using System;

using UnityEngine;

#nullable enable

[Serializable]
class RenderTextureManager
{
    [SerializeField] private ComputeShader computeShader = default!;
    [SerializeField] private Vector2Int textureSize = new Vector2Int(512, 512);
    [SerializeField] private int depthBufferSize = 24;
    [SerializeField] private float brushSize = 10.0f;

    private RenderTexture renderTexture = default!;

    public RenderTexture? CreateRenderTexture()
    {
        if(computeShader == null)
        {
            Debug.LogError("Component disabled: ComputeShader is not attached");
            return null;
        }

        renderTexture = new RenderTexture(textureSize.x, textureSize.y, depthBufferSize);
        renderTexture.filterMode = FilterMode.Point;
        renderTexture.enableRandomWrite = true;
        renderTexture.Create();

        Clear();

        return renderTexture;
    }

    public void Clear()
    {
        var initBackgroundKernel = computeShader.FindKernel("InitBackground");
        computeShader.SetFloat("_BrushSize", brushSize);
        computeShader.SetTexture(initBackgroundKernel, "_Whiteboard", renderTexture);
        computeShader.Dispatch(initBackgroundKernel, renderTexture.width / 8, renderTexture.height / 8, 1);
    }

    public Texture2D GetTexture()
    {
        var texture = new Texture2D(renderTexture.width, renderTexture.height);
        texture.ReadPixels(new Rect(0, 0, renderTexture.width, renderTexture.height), 0, 0);
        texture.Apply();

        return texture;
    }

    public void DrawPoint(Vector2 normalizedPoint)
    {
        var point = normalizedPoint * textureSize;
        var drawPointKernel = computeShader.FindKernel("DrawPoint");
        computeShader.SetVector("_Position1", point);
        computeShader.SetTexture(drawPointKernel, "_Whiteboard", renderTexture);
        computeShader.Dispatch(drawPointKernel, renderTexture.width / 8, renderTexture.height / 8, 1);
    }

    public void DrawLine(Vector2 normalizedPoint1, Vector2 normalizedPoint2)
    {
        var point1 = normalizedPoint1 * textureSize;
        var point2 = normalizedPoint2 * textureSize;

        var drawLineKernel = computeShader.FindKernel("DrawLine");
        computeShader.SetVector("_Position1", point1);
        computeShader.SetVector("_Position2", point2);
        computeShader.SetTexture(drawLineKernel, "_Whiteboard", renderTexture);
        computeShader.Dispatch(drawLineKernel, renderTexture.width / 8, renderTexture.height / 8, 1);
    }
} 
