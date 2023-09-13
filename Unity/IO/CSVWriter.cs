#nullable enable

using System;
using System.Linq;

class CSVWriter : MovementHistorySaver.IMovementHistorySaverComponent
{
    private readonly string filename;
    private readonly string labelLineText;

    private readonly Func<object[][]?> GetData;

    private readonly ITargetDirectoryManager targetDirectoryManager;
    private readonly StreamWriterWrapper streamWriterWrapper = new();

    internal CSVWriter(
        string filename, string labelLineText, Func<object[][]?> GetData, 
        ITargetDirectoryManager targetDirectoryManager)
    {
        this.filename = filename;
        this.labelLineText = "Timestamp, " + labelLineText;

        this.GetData = GetData;
        
        this.targetDirectoryManager = targetDirectoryManager;
    }

    internal event Action? Opened;
    internal event Action? Closed;

    bool MovementHistorySaver.IMovementHistorySaverComponent.TryOpen(out string errorMessage)
    {
        var filePath = targetDirectoryManager.GetFilePath(filename);

        var succeeded = streamWriterWrapper.TryOpen(filePath, out errorMessage) && streamWriterWrapper.TryWriteLine(labelLineText, out errorMessage);
        if(succeeded)
        {
            Opened?.Invoke();
        }

        return succeeded;
    }

    bool MovementHistorySaver.IMovementHistorySaverComponent.TrySaveUpdatedData(float timestamp, out string errorMessage)
    {
        errorMessage = "";

        var data = GetData();
        if(data == null || data.Count() == 0)
        {
            return true;
        }

        var dataLineStrings = data.Select(dataLine => timestamp + ", " + string.Join(", ", dataLine.Select(data => data.ToString())));
        var dataString = string.Join(Environment.NewLine, dataLineStrings);

        return streamWriterWrapper.TryWriteLine(dataString, out errorMessage);
    }

    bool MovementHistorySaver.IMovementHistorySaverComponent.TryClose(out string errorMessage)
    {
        var succeeded = streamWriterWrapper.TryClose(out errorMessage);
        Closed?.Invoke();
        return succeeded;
    }
}

class CSVInitialDataWriter : MovementHistorySaver.IInitialDataSaveComponent
{
    private readonly string filename; 
    private readonly Func<(string label, object data)[]?> GetDataList;

    private readonly ITargetDirectoryManager targetDirectoryManager;
    private readonly StreamWriterWrapper streamWriterWrapper;

    internal CSVInitialDataWriter(string filename, Func<(string label, object data)[]?> GetDataList, ITargetDirectoryManager targetDirectoryManager, StreamWriterWrapper streamWriterWrapper)
    {
        this.filename = filename;

        this.GetDataList = GetDataList;
        
        this.targetDirectoryManager = targetDirectoryManager;
        this.streamWriterWrapper = streamWriterWrapper;
    }

    bool MovementHistorySaver.IInitialDataSaveComponent.TrySaveInitialData(out string errorMessage)
    {
        errorMessage = "";

        var filePath = targetDirectoryManager.GetFilePath(filename);

        var dataList = GetDataList();
        if(dataList == null)
        {
            return true;
        }
        var text = string.Join('\n', dataList.Select(data => $"{data.label}, {data.data}"));

        if(!streamWriterWrapper.TryOpen(filePath, out errorMessage))
        {
            return false;
        }

        var writeSucceeded = streamWriterWrapper.TryWriteLine(text, out errorMessage);

        if(!streamWriterWrapper.TryClose(out var errorMessageWhileClosing))
        {
            errorMessage += errorMessageWhileClosing;
            return false;
        }

        return writeSucceeded;
    }
}
