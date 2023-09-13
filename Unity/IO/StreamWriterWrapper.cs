#nullable enable

using System;
using System.IO;

class StreamWriterWrapper : IDisposable
{
    private StreamWriter? streamWriter;

    internal bool TryOpen(string filePath, out string errorMessage)
    {
        if(!TryClose(out errorMessage))
        {
            return false;
        }

        try
        {
            var directoryPath = Path.GetDirectoryName(filePath);
            if (!Directory.Exists(directoryPath))
            {
                Directory.CreateDirectory(directoryPath);
            }

            streamWriter = new(filePath);

            errorMessage = "";
            return true;
        }
        catch(UnauthorizedAccessException ex)
        {
            errorMessage = $"Unauthorized access while initializing StreamWriter. {ex.Message}\nStackTrace: \n{ex.StackTrace}";
        }
        catch (IOException ex)
        {
            errorMessage = $"IO error while initializing StreamWriter. {ex.Message}\nStackTrace: \n{ex.StackTrace}";
        }

        return false;
    }

    internal bool TryWriteLine(string text, out string errorMessage)
    {
        if(streamWriter == null)
        {
            errorMessage = "File not opened.";
            return false;
        }

        try
        {
            streamWriter!.WriteLine(text);

            errorMessage = "";
            return true;
        }
        catch(IOException ex)
        {
            errorMessage = $"IO error while writing data. {ex.Message}\nStackTrace: \n{ex.StackTrace}";
        }
        catch(ObjectDisposedException ex)
        {
            errorMessage = $"StreamWriter has been closed. {ex.Message}\nStackTrace: \n{ex.StackTrace}";
        }

        return false;
    }

    internal bool TryClose(out string errorMessage)
    {
        try
        {
            streamWriter?.Close();
            streamWriter = null;

            errorMessage = "";
            return true;
        }
        catch (IOException ex)
        {
            errorMessage = $"IO error while closing StreamWriter. {ex.Message}\nStackTrace: \n{ex.StackTrace}";
            return false;
        }            
    }

    public void Dispose()
    {
        TryClose(out var _);
    }
}
