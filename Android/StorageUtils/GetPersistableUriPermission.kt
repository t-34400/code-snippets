class MainActivity : AppCompatActivity() {
    private val launcher = registerForActivityResult(
        ActivityResultContracts.GetContent()
    ) { uri ->
        uri?.let{
            val takeFlags: Int = Intent.FLAG_GRANT_READ_URI_PERMISSION or Intent.FLAG_GRANT_WRITE_URI_PERMISSION
            context.contentResolver.takePersistableUriPermission(it, takeFlags)
        }
    }

    fun getPersistableUri() {
        launcher.launch("image/*")
    }
}