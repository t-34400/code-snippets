using UnityEngine;
using System.Collections.Generic;
using System.IO;

public class SaveManager : MonoBehaviour
{
    [System.Serializable]
    public class SaveData
    {
        public int ID;
        public Vector3 Position;
        public Quaternion Rotation;
    }

    [SerializeField]
    private List<SaveData> saveList = new List<SaveData>();

    private string savePath;

    private void Awake()
    {
        savePath = Application.persistentDataPath + "/saveData.json";
    }

    public void Save()
    {
        try
        {
            string json = JsonUtility.ToJson(saveList);

            File.WriteAllText(savePath, json);
            Debug.Log("Saved the game data");
        }
        catch (System.Exception e)
        {
            Debug.LogError("An error occurred while saving the game data: " + e.Message);
        }
    }

    public void Load()
    {
        if (File.Exists(savePath))
        {
            try
            {
                string json = File.ReadAllText(savePath);

                saveList = JsonUtility.FromJson<List<SaveData>>(json);
                Debug.Log("Loaded the game data");
            }
            catch (System.Exception e)
            {
                Debug.LogError("An error occurred while loading the game data: " + e.Message);
            }
        }
        else
        {
            Debug.LogWarning("No game data found");
        }
    }
}
