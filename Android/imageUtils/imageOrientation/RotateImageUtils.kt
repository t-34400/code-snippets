import java.io.ByteArrayinputStream
import java.io.ByteArrayOutputStream
import java.io.InputStream

import android.media.ExifInterface
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.graphics.Matrix


fun getOrientationOfImageFromInputStream(inputStream: InputStream): Int {
   val exifInterface = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
        ExifInterface(inputStream)
    } 
    // If the device's Android version is earlier than Nougat, create an ExifInterface instance using the input stream if it is not null.
    else {
        inputStream?.let {
            ExifInterface(inputStream)
        }
    }

    return when (exifInterface?.getAttributeInt(ExifInterface.TAG_ORIENTATION, ExifInterface.ORIENTATION_NORMAL)) {
        ExifInterface.ORIENTATION_ROTATE_90 -> 90
        ExifInterface.ORIENTATION_ROTATE_180 -> 180
        ExifInterface.ORIENTATION_ROTATE_270 -> 270
        else -> 0
    }
}

fun getRotatedInputStream(inputStream: InputStream, orientation: Int): InputStream {
    val bitmap = BitmapFactory.decodeStream(inputStream)
    val matrix = Matrix().apply {
        postRotate(orientation.toFloat())
    }
    val rotatedBitmap = Bitmap.createBitmap(
            source=bitmap, 
            x=0, y=0, 
            width=bitmap.width, 
            height=bitmap.height, 
            m=matrix, 
            filter=true
        )
    val outputStream = ByteArrayOutputStream()
    rotatedBitmap.compress(Bitmap.CompressFormat.JPEG, 100, outputStream)
    val byteArray = outputStream.toByteArray()
    return ByteArrayInputStream(byteArray)
}
