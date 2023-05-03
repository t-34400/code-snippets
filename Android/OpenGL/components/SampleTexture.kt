import android.graphics.Bitmap
import android.opengl.GLES30

import xxx.xxx.xxx.GLLog

/**
 * This class should be instantiated on the GL thread.
 */
class SampleTexture(
    bitmaps: List<Bitmap>,
    val textureSlot: Int = GLES30.GL_TEXTURE0
) {
    val textureCount = bitmaps.count()
    val textureIds: IntArray = IntArray(textureCount)
    
    init {
        GLES30.glActiveTexture(textureSlot)
        GLES30.glGenTextures(textureCount, textureIds, 0)
        GLLog.checkGLError("glGenTextures")

        bitmaps.forEachIndexed { i, bitmap ->
            GLES30.glBindTexture(GLES30.GL_TEXTURE_2D, textureIds[i])
            GLLog.checkGLError("glBindTexture")
            
            // GL_LINEAR: Returns the weighted average of the four texture elements that are closest to the center of the pixel being textured. 
            // Ref: https://registry.khronos.org/OpenGL-Refpages/es2.0/xhtml/glTexParameter.xml
            GLES30.glTexParameteri(GLES30.GL_TEXTURE_2D, GLES30.GL_TEXTURE_MAG_FILTER, GLES30.GL_LINEAR)
            GLES30.glTexParameteri(GLES30.GL_TEXTURE_2D, GLES30.GL_TEXTURE_MIN_FILTER, GLES30.GL_LINEAR)
            GLES30.glTexParameteri(GLES30.GL_TEXTURE_2D, GLES30.GL_TEXTURE_WRAP_S, GLES30.GL_REPEAT)
            GLES30.glTexParameteri(GLES30.GL_TEXTURE_2D, GLES30.GL_TEXTURE_WRAP_T, GLES30.GL_REPEAT)
            GLLog.checkGLError("glTexParameteri")

            // Specifies the level-of-detail number. Level 0 is the base image level. Level n is the nth mipmap reduction image.
            // Ref: https://registry.khronos.org/OpenGL-Refpages/es2.0/xhtml/glTexImage2D.xml
            val level = 0
            GLUtils.texImage2D(GLES30.GL_TEXTURE_2D, 0, bitmap, 0)
            GLLog.checkGLError("texImage2D")
            GLES30.glBindTexture(GLES30.GL_TEXTURE_2D, 0)
            GLLog.checkGLError("glBindTexture")
        }
    }

    fun updateImage(
        newBitmap: Bitmap, 
        textureIndex: Int = 0,
    ) {
        val level = 0
        val xOffset = 0
        val yOffset = 0

        GLES30.glActiveTexture(textureSlot)
        GLES30.glBindTexture(GLES30.GL_TEXTURE_2D, textureIds[textureIndex])
        GLUtils.texSubImage2D(GLES30.GL_TEXTURE_2D, level, xOffset, yOffset, newBitmap)
        GLES30.glBindTexture(GLES30.GL_TEXTURE_2D, 0)
    }

    fun bindTexture(textureIndex: Int = 0) {
        GLES30.glActiveTexture(textureSlot)
        GLES30.glBindTexture(GLES30.GL_TEXTURE_2D, textureIds[textureIndex])
    }

    fun unbindTexture() {
        GLES30.glBindTexture(GLES30.GL_TEXTURE_2D, 0)
    }
}