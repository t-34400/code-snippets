import javax.microedition.khronos.opengles.GL10

import android.graphics.Bitmap
import android.opengl.GLES30
import android.opengl.GLSurfaceView.Renderer
import android.opengl.Matrix

import xxx.xxx.xxx.GLLog
import xxx.xxx.xxx.TextureShader
import xxx.xxx.xxx.SampleMesh


class SampleRenderer: GLSurfaceView.Renderer {
    companion object {
        private const val CLEAR_COLOR_R = 0.1f
        private const val CLEAR_COLOR_G = 0.1f
        private const val CLEAR_COLOR_B = 0.1f
        private const val CLEAR_COLOR_A = 0.9f
        private const val VERTICAL_FOV_IN_DEG = 72.0f
        private const val Z_NEAR = 0.1f
        private const val Z_FAR = 10.0f

        private data class Point3D(val x: Float, val y: Float, val z: Float)
    }

    // Temporary matrix for storing calculated values
    private val projectionMatrix = FloatArray(16)
    private val viewMatrix = FloatArray(16)

    private val vpMatrix = FloatArray(16)
    
    private var cameraPosition = Point3D(1.0f, 0.0f, 0.0f)
    private var cameraTarget = Point3D(0.0f, 0.0f, 0.0f)
    private val cameraUpVector = Point3D(0.0f, 0.1f, 0.0f)

    private var _textureShader: TextureShader? = null
    private var _mesh: SampleMesh? = null
    private var _texture: SampleTexture? = null

    private val textureShader: TextureShader get() = _textureShader!!
    private val mesh: SampleMesh get() = _mesh!!
    private val texture: SampleTexture get() = _texture!!

    override fun onSurfaceCreated(unused: GL10, config: EGLConfig) {
        GLES30.glClearColor(CLEAR_COLOR_R, CLEAR_COLOR_G, CLEAR_COLOR_B, CLEAR_COLOR_A)
        _textureShader = TextureShader()
        _mesh = Mesh()
        bitmaps: List<Bitmap> = listOf( ... )
        _texture = SampleTexture(bitmaps, GLES30.GL_TEXTURE0)
    }

    override fun onSurfaceChanged(unused: GL10, width: Int, height: Int) {
        GLES30.glViewport(0, 0, width, height)
        val offset = 0
        val aspect = width.toFloat() / height
        Matrix.perspectiveM(projectionMatrix, offset, VERTICAL_FOV_IN_DEG, aspect, Z_NEAR, Z_FAR)
    }

    override fun onDrawFrame(unused: GL10) {
        GLES30.glClear(GLES30.GL_COLOR_BUFFER_BIT)

        // calculate View-Projection Matrix
        val viewOffset = 0
        Matrix.setLookAtM(
            viewMatrix, viewOffset,
            cameraPosition.x, cameraPosition.y, cameraPosition.z,
            cameraTarget.x, cameraTarget.y, cameraTarget.z,
            cameraUpVector.x, cameraUpVector.y, cameraUpVector.z
        )
        val projectionOffset = 0
        val vpOffset = 0
        Matrix.multiplyMM(
            vpMatrix, vpOffset,
            projectionMatrix, projectionOffset,
            viewMatrix, viewOffset
        )

        GLES30.glColorMask(true, true, true, true)
        GLES30.glUseProgram(textureProgram)
        // Shader: (set attributes and uniforms)
        activateTextureSlot(textureProgram)
        GLES30.glBindTexture(GLES30.GL_TEXTURE_2D, textureIds[0])
        // Mesh: draw
    }

}
