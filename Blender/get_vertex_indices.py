import bpy


def get_array_of_vert_indices_in_group(vertex_group_name):
    obj = bpy.context.active_object
    vertex_group = obj.vertex_groups[vertex_group_name]
    verts_in_group = []
    for vert in obj.data.vertices:
        for group in vert.groups:
            if(group.group == vertex_group.index):
                verts_in_group.append(vert)
    return [vert.index for vert in  verts_in_group]

def select_verts_in_group(vertex_group_name, append_mode=False):
    try:
        bpy.ops.object.mode_set(mode = 'OBJECT')
    except:
        pass 
    obj = bpy.context.active_object
    bpy.ops.object.mode_set(mode = 'EDIT') 
    bpy.ops.mesh.select_mode(type="VERT")
    if not append_mode:
        bpy.ops.mesh.select_all(action = 'DESELECT')
    bpy.ops.object.mode_set(mode = 'OBJECT')
    target_group =obj.vertex_groups[vertex_group_name]
    for vert in obj.data.vertices:
        for group in vert.groups:
            if(group.group == target_group.index):
                vert.select = True
    bpy.ops.object.mode_set(mode = 'EDIT')