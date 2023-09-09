#nullable enable

using System;
using System.IO;
using UnityEngine;

public class SubdirectoryLister : MonoBehaviour
{
    private const string dataDirectoryName = "Data";

    void Start()
    {
        var dataPath = Path.Join(Application.dataPath, dataDirectoryName);

        try
        {
            var subdirectories = Directory.GetDirectories(dataPath);

            foreach (var subdirectory in subdirectories)
            {
                Debug.Log("Subdirectory: " + subdirectory);
            }
        }
        catch (DirectoryNotFoundException ex)
        {
            Debug.LogError("Directory not found: " + ex.Message);
        }
        catch (IOException ex)
        {
            Debug.LogError("IO error: " + ex.Message);
        }
        catch (UnauthorizedAccessException ex)
        {
            Debug.LogError("Unauthorized access: " + ex.Message);
        }
        catch (Exception ex)
        {
            Debug.LogError("An error occurred: " + ex.Message);
        }
    }
}
