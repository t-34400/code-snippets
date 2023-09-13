#nullable enable

using UnityEngine;

public class CameraLookRotation : MonoBehaviour
{
    [SerializeField] private Transform targetObject = default!;

    [SerializeField] private float sensitivity = 2.0f;
    [SerializeField] private float zoomSpeed = 0.5f;
    
    [SerializeField] private float minDistance = 1.0f;
    [SerializeField] private float maxDistance = 5.0f;

    [SerializeField] private float minAngleX = 0.0f;
    [SerializeField] private float maxAngleX = 75.0f;

    private float currentDistance = default!;

    private void Start()
    {
        var offset = transform.position - targetObject.position;
        
        currentDistance = offset.magnitude;

        UpdateTransform();
    }

    private void Update()
    {
        if (Input.GetMouseButton(1))
        {
            var mouseDelta = new Vector2(Input.GetAxis("Mouse X"), Input.GetAxis("Mouse Y"));
            var rotationDelta = mouseDelta * sensitivity;

            transform.rotation *= Quaternion.Euler(-rotationDelta.y, rotationDelta.x, 0.0f);
        }

        var scroll = Input.GetAxis("Mouse ScrollWheel");
        currentDistance -= scroll * zoomSpeed;

        UpdateTransform();
    }

    private void UpdateTransform()
    {
        currentDistance = Mathf.Clamp(currentDistance, minDistance, maxDistance);
        
        var rotationEuler = transform.rotation.eulerAngles;
        if(rotationEuler.x > 180.0f || rotationEuler.x < minAngleX)
        {
            rotationEuler.x = minAngleX;
        }
        else if(rotationEuler.x > maxAngleX)
        {
            rotationEuler.x = maxAngleX;
        }
        transform.rotation = Quaternion.Euler(rotationEuler);

        var offset = transform.rotation * new Vector3(0.0f, 0.0f, currentDistance);

        transform.position = targetObject.position - offset;
        transform.rotation = Quaternion.LookRotation(offset, Vector3.up);
    }

    private void OnValidate()
    {
        minDistance = Mathf.Clamp(minDistance, 0.1f, maxDistance);
        maxDistance = Mathf.Max(minDistance, maxDistance);

        minAngleX = Mathf.Clamp(minAngleX, -90.0f, 90.0f);
        maxAngleX = Mathf.Clamp(maxAngleX, minAngleX, 90.0f);
    }
}
