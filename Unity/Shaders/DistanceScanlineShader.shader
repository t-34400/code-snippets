Shader "Custom/DistanceScanlineShader"
{
    // Note: (Line Speed) / (Frequency) should be greater than Line Width.
    Properties {
        _MainColor ("Main Color", Color) = (1, 1, 1, 1)
        _LineColor ("Scan Line Color", Color) = (1, 0, 0, 1)
        _LineWidth ("Line Width", Range(0.001, 100)) = 0.2
        _LineSpeed ("Line Speed", Range(0.001, 100)) = 1
        _Frequency ("Frequency", Range(0.001, 100)) = 1
    }

    SubShader {
        Tags { "RenderType"="Transparent" "Queue"="Transparent" }
        LOD 200

        CGPROGRAM
        #pragma surface surf Lambert alpha

        fixed4 _MainColor;
        fixed4 _LineColor;
        float _LineWidth;
        float _LineSpeed;
        float _Frequency;

        struct Input {
            float3 worldPos;
        };

        float GetShortestDistanceToPeriodicPoint(float currentTime, float distanceFromCamera)
        {
            float waveLength = _LineSpeed / _Frequency;
            float tempDistance = _LineSpeed * currentTime - distanceFromCamera;

            return abs(frac((tempDistance + waveLength / 2) / waveLength) * waveLength - waveLength / 2);
        }

        void surf (Input IN, inout SurfaceOutput o) {
            float currentTime = _Time.z;
            float distanceFromCamera = distance(_WorldSpaceCameraPos, IN.worldPos);

            float t = 1 - GetShortestDistanceToPeriodicPoint(currentTime, distanceFromCamera) / _LineWidth;
            t = min(1, max(0, t));
            fixed4 finalColor = lerp(_MainColor, _LineColor, t);

            o.Albedo = finalColor.rgb;
            o.Alpha = finalColor.a;
        }

        ENDCG
    }
    FallBack "Diffuse"
}
