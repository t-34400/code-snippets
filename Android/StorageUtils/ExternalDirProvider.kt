class ExternalDirProvider {

    fun getExternalFilesDir(context: Context): File {  
        return if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
            // On Android 11 and above, use the new API to access external storage
            // DIRECTORY_DCIM, DIRECTORY_DOWNLOADS, etc.
            context.getExternalFilesDir(Environment.DIRECTORY_DOCUMENTS)
        } else {
            // On earlier versions of Android, use the legacy API to access external storage
            Environment.getExternalStorageDirectory()
        }
    }
}

