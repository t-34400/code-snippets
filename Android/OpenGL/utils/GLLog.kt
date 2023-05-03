object GLLog {

    fun checkGLError(operation: String) {
        val error = GLES30.glGetError()
        if (error != GLES30.GL_NO_ERROR) {
            // error handling
        }
    }

}
