import android.content.Context
import android.opengl.GLSurfaceView

import xxx.xxx.xxx.SampleRenderer

class MyGLSurfaceView(context: Context) : GLSurfaceView(context) {

    private val renderer: SampleRenderer? = null

    init {
        if(isGLESVersionSupported(context)) {
            renderMode = GLSurfaceView.RENDERMODE_WHEN_DIRTY
            setEGLContextClientVersion(3)
            renderer = SampleRenderer()
            setRenderer(renderer)
        }
    }

    private fun isGLESVersionSupported(context: Context) : Boolean {
        val activityManager = context.getSystemService(Context.ACTIVITY_SERVICE) as ActivityManager
        val deviceConfigurationInfo = activityManager.deviceConfigurationInfo
        val glVersion = deviceConfigurationInfo.glEsVersion
        return glVersion > "0x00030000" // check if GLES 3.0 is supported
    }

    fun render() {
        // runnable to be run on the GL thread.
        val runnable = { ... }
        queueEvent(runnable)
        requestRender()
    }
}
