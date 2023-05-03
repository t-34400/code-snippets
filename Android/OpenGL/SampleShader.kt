import android.opengl.GLES30

import xxx.xxx.xxx.GLLog

object ShaderUtils {
    
    data class ShaderSource(
        val vertexShaderCode: String,
        val fragmentShaderCode: String,
        val attributes: List<String>,
    )

    fun createProgram(shaderSource: ShaderSource): Int {
        val vertexShader = compileShader(GLES30.GL_VERTEX_SHADER, shaderSource.vertexShaderCode)
        val fragmentShader = compileShader(GLES30.GL_FRAGMENT_SHADER, shaderSource.fragmentShaderCode)

        val program = GLES30.glCreateProgram()
        if(program == GL_FALSE) {
            // error handling
        }
        GLES30.glAttachShader(program, vertexShader)
        GLLog.checkGLError("glAttachShader")
        GLES30.glAttachShader(program, fragmentShader)
        GLLog.checkGLError("glAttachShader")

        shaderSource.attributes.forEachIndexed { index, attribute ->
            GLES30.glBindAttribLocation(program, index, attribute)
            GLLog.checkGLError("glBindAttribLocation")
        }

        GLES30.glLinkProgram(program)
        val linked = IntArray(1)
        GLES30.glGetProgramiv(program, GLES30.GL_LINK_STATUS, linked, 0)
        if (linked[0] == GL_FALSE) {
            GLES30.glDeleteProgram(programObject)
            // error handling
        }
    }

    private fun compileShader(type: Int, shaderCode): Int {
        val shader = GLES30.glCreateShader(type)
        if(shader == GL_FALSE) {
            // error handling
        }

        GLES30.glShaderSource(shader, shaderCode)
        GLES30.glCompileShader(shader)

        // check compile status
        val compiled = IntArray(1)
        GLES30.glGetShaderiv(shader, GLES30.GL_COMPILE_STATUS, compiled, 0)
        if (compiled[0] == GL_FALSE) {
            val infoLog = GLES30.glGetShaderInfoLog(shader)
            GLES30.glDeleteShader(shader)
            // error handling
        }
    }
}


class TextureShader {
    companion object {
        const val VERTEX_POSITION_ATTRIBUTE_NAME = "aPosition"
        const val VERTEX_UV_ATTRIBUTE_NAME = "aTexCoord"
        const val VERTEX_NORMAL_ATTRIBUTE_NAME = "aNormal"

        const val MODEL_MATRIX_UNIFORM_NAME = "uModelMatrix"
        const val VIEW_PROJECTION_MATRIX_UNIFORM_NAME = "uVPMatrix"

        const val TEXTURE_UNIFORM_NAME = "uTexture"
        const val LIGTH_POSITION_UNIFORM_NAME = "uLightPosition"
        const val LIGHT_COLOR_UNIFORM_NAME = "uLightColor"

        private const val VERTEX_POSITION_VARYING_NAME = "vPosition"
        private const val VERTEX_UV_VARYING_NAME = "vTexCoord"
        private const val VERTEX_NORMAL_VARYING_NAME = "vNormal"
        
        private val vertexShaderCode = """
            #version 300 es

            in vec3 $VERTEX_POSITION_ATTRIBUTE_NAME;
            in vec2 $VERTEX_UV_ATTRIBUTE_NAME;
            in vec3 $VERTEX_NORMAL_ATTRIBUTE_NAME;

            uniform mat4 $MODEL_MATRIX_UNIFORM_NAME;
            uniform mat4 $VIEW_PROJECTION_MATRIX_UNIFORM_NAME;

            out vec3 $VERTEX_POSITION_VARYING_NAME;
            out vec2 $VERTEX_UV_VARYING_NAME;
            out vec3 $VERTEX_NORMAL_VARYING_NAME;

            void main() {
                vec4 worldPosition = $MODEL_MATRIX_UNIFORM_NAME * vec4($VERTEX_POSITION_ATTRIBUTE_NAME, 1.0);
                gl_Position = $VIEW_PROJECTION_MATRIX_UNIFORM_NAME * worldPosition;
                $VERTEX_POSITION_VARYING_NAME = worldPosition;
                $VERTEX_UV_VARYING_NAME = $VERTEX_POSITION_ATTRIBUTE_NAME;
                $VERTEX_NORMAL_VARYING_NAME = $VERTEX_NORMAL_ATTRIBUTE_NAME;
            }
        """.trimIndent()

        private val fragmentShaderCode = """
            #version 300 es
            precision mediump float;

            uniform sampler2D $TEXTURE_UNIFORM_NAME;
            uniform vec3 $LIGTH_POSITION_UNIFORM_NAME;
            uniform vec3 $LIGTH_COLOR_UNIFORM_NAME;

            in vec3 $VERTEX_POSITION_VARYING_NAME;
            in vec2 $VERTEX_UV_VARYING_NAME;
            in vec3 $VERTEX_NORMAL_VARYING_NAME;

            void main() {
                vec4 texColor = texture2D($TEXTURE_UNIFORM_NAME, $VERTEX_UV_VARYING_NAME);

                vec3 ambient = texColor.rgb * 0.3;
                vec3 lightDirection = normalize($LIGTH_POSITION_UNIFORM_NAME - $VERTEX_POSITION_VARYING_NAME);
                float cosTheta = dot(lightDirection, $VERTEX_NORMAL_VARYING_NAME);
                vec3 diffuse = texColor.rgb * max(cosTheta, 0.0);
                vec3 reflection = reflect(lightDirection, $VERTEX_NORMAL_VARYING_NAME);
                vec3 specular = pow(max(dot(reflection, normalize($VERTEX_POSITION_VARYING_NAME)), 0.0), 16.0) * $LIGTH_COLOR_UNIFORM_NAME;

                vec3 color = ambient + diffuse + specular;
                gl_FragColor = vec4(color, 1.0);
            }
        """.trimIndent()

        private val attributes = lisfOf(
            VERTEX_POSITION_ATTRIBUTE_NAME,
            VERTEX_UV_ATTRIBUTE_NAME,
            VERTEX_NORMAL_ATTRIBUTE_NAME
        )

        private val shaderSource get() = ShaderUtils.ShaderSource(
            vertexShaderCode,
            fragmentShaderCode,
            attributes,
        )
    }

    private val program = ShaderUtils.createProgram(shaderSource)

    fun getAttribLocation(attribName: String): Int {
        return GLES30.glGetAttribLocation(program, attribName)
    }

    fun getUniformLocation(uniformName: String): Int {
        return GLES30.glGetUniformLocation(program, uniformName)
    }
}