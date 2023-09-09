#nullable enable

using UnityEngine;

public class CameraLookRotation : MonoBehaviour
{
    [SerializeField] private transfotm targetObject = default!;

    [SerializeField] private float sensitivity = 2.0f;
    [SerializeField] private float zoomSpeed = 0.5f;
    
    [SerializeField] private float minDistance = 1.0f;
    [SerializeField] private float maxDistance = 5.0f;

    [SerializeField] private float minAngleX = 0.0f;
    [SerializeField] private float maxAngleX = 75.0f;

    private Vector3 currentDistance = default!;
    private Quaternion currentRotation = default!;

    private void Start()
    {
        var offset = transform.position - targetObject.position;
        
        currentDistance = offset.magnitude;
        currentRotation = Quaternion.FromToRotation(Vector3.forward, offset);

        UpdateTransform();
    }

    private void Update()
    {
        if (Input.GetMouseButton(2))
        {
            var mouseDelta = new Vector2(Input.GetAxis("Mouse X"), Input.GetAxis("Mouse Y"));
            var rotationDelta = mouseDelta * sensitivity;

            currentRotation = Quaternion.Euler(rotationDelta.x, rotationDelta.y, 0.0f) * currentRotation;
        }

        var scroll = Input.GetAxis("Mouse ScrollWheel");
        currentDistance -= scroll * zoomSpeed;

        UpdateTransform();
    }

    private void UpdateTransform()
    {
        currentDistance = Mathf.Clamp(currentDistance, minDistance, maxDistance);
        
        var rotationEuler = currentRotation.eulerAngles;
        rotationEuler.x = Mathf.Clamp(rotationEuler.x, minAngleX, maxAngleX);
        currentRotation = Quaternion.Euler(rotationEuler);

        offset = currentRotation * new Vector3(0.0f, 0.0f, currentDistance);
        transform.position = targetObject.position + offset;
    }

    private void OnValidate()
    {
        minDistance = Mathf.Clamp(minDistance, 0.1f, maxDistance);
        maxDistance = Mathf.Max(minDistance, maxDistance);

        minAngleX = Mathf.Clamp(minAngleX, -90.0f, 90.0f);
        maxAngleX = Mathf.Clamp(maxAngleX, minAngleX, 90.0f);
    }
}
