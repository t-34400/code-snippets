import bpy
from mathutils import Vector

from random import random

def set_keyframe_for_vertex_coordinates():
    target_object_name = "Cube"
    target_frame = 2
    vertex_count = 8
    new_coordinates = [Vector(random(), random(), random()) for _ in range(0, vertex_count)]

    mesh = bpy.data.objects[target_object_name].data
    for vert in mesh.vertices:
        new_coord = new_coordinates[vert.index]
        vert.co = new_coord
        vert.keyframe_insert("co", frame=target_frame)
