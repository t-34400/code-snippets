import java.nio.IntBuffer
import java.nio.FloatBuffer

/**
 * This class should be instantiated on the GL thread.
 */
class SampleMesh {
    companion object {
        private const val VERTEX_DIMENSION = 3
        private const val UV_DIMENSION = 2
        private const val NORMAL_DIMENSION = 3

        private val dimensions = listOf(VERTEX_DIMENSION, UV_DIMENSION, NORMAL_DIMENSION)

        data class VertexBuffers (
            val vertexBuffer: FloatBuffer,
            val uvBuffer: FloatBuffer,
            val NormalBuffer: FloatBuffer,
        ) {
            init {
                // [vertex count] x [size of Float]
                vertexCounts = toList().mapIndexed { i, buffer ->
                    val bufferSize = buffer.rewind().remaining()
                    val dimension = dimensions[i]
                    return@mapIndexed bufferSize / dimension
                }
                val isAllSame = vertexCounts.distinct().size == 1
                if(!isAllSame) {
                    // error handing
                }
            }

            fun toList(): List<FloatBuffer> {
                return listOf(vertexBuffer, uvBuffer, normalBuffer)
            }
        }

        data class AttribLocations (
            vertex: Int,
            uv: Int,
            normal: Int,
        ) {
            fun toList(): List<Int> {
                return listOf(vertex, uv, normal)
            }
        }

        private data class VertexBufferObject (
            val dimension: Int,
            val bufferSize: Int,
            val bufferObject: Int,
        )
    }

    private var bufferObjects: List<VertexBufferObject>
    private val vertexCount: Int,

    init {
        val vertexBuffers: VertexBuffers = ...

        val buffers = vertexBuffers.toList()

        val bufferObjectBuffer = InfBuffer.allocate(3)
        GLES30.glGenBuffers(3, bufferObjectBuffer)
        
        bufferObjects = (0..2).map { i ->
            val floatSize = 4
            val bufferSize = buffers[i].rewind().remaining()
            GLES30.glBindBuffer(GLES30.GL_ARRAY_BUFFER, bufferObjectBuffer[i])
            // use GLES30.GL_DYNAMIC_DRAW if you frequently update vertex data.
            GLES30.glBufferData(GLES30.GL_ARRAY_BUFFER, bufferSize*floatSize, buffers[i], GLES30.GL_STATIC_DRAW)
            GLES30.glBindBuffer(GLES30.GL_ARRAY_BUFFER, 0)
            return@map VertexBufferObject(SampleMesh.dimensions[i], bufferSize, bufferObjectBuffer[i])
        }

        vertexCount = bufferObjects[0].bufferSize / bufferObjects[0].dimension
    }

    fun updateVertex(newBuffers: VertexBuffers) {
        val newBufferList = newBuffers.toList()

        bufferObjects = bufferObjects.mapIndexed { i, bufferObject ->
            val offset = 0
            val floatSize = 4
            GLES30.glBindBuffer(GLES30.GL_ARRAY_BUFFER, bufferObject.bufferObject)
            GLES30.glBufferSubData(GLES30.GL_ARRAY_BUFFER, offset, bufferObject.bufferSize, newBufferList[i])
            GLES30.glBindBuffer(GLES30.GL_ARRAY_BUFFER, 0)
            return@map VertexBufferObject(bufferObjects[i].dimension, bufferObject.bufferSize, bufferObject.bufferObject)
        }
    }

    fun draw(attribLocations: AttribLocations) {
        bufferObjects.forEachIndexed { i, bufferObject ->
            val normalized = false
            val stride = 0
            val offset = 0
            val attribLocation = attribLocations[i]
            GLES30.glEnableVertexAttribArray(attribLocation)
            GLES30.glBindBuffer(GLES30.GL_ARRAY_BUFFER, bufferObject.bufferObject)
            GLES30.glEnableVertexAttribArray(attribLocation)
            GLES30.glVertexAttribPointer(attribLocation, bufferObject.dimension, GLES30.GL_FLOAT, normalized, stride, offset)
            GLES30.glBindBuffer(GLES30.GL_ARRAY_BUFFER, 0)
        }

        val offset = 0
        GLES30.glDrawArrays(GLES30.GL_TRIANGLES, offset, vertexCount)
        attribLocations.forEach { attribLocation ->
            GLES30.glDisableVertexAttribArray(attribLocation)
        }
    }
}