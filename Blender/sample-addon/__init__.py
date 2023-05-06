bl_info = {
    "name": "Sample Add-on",
    "description": "Sample Add-on for Blender",
    "author": "t-34400",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar > Sample Panel Tab",
    "category": "Mesh"
}


modules = (
    'sample_operator',
    'sample_panel_properties',
    'sample_panel'
)

# When reloading a script, only __init__.py is reloaded, 
# so it is necessary to explicitly reload other modules within __init__.py.
if "bpy" in locals():
    import importlib
    for module_name in modules:
        module = importlib.import_module(module_name, package=__name__)
        importlib.reload(module)
    print('reload classes')


import bpy
from sample_operator import Sample_Operator
from sample_panel_properties import Sample_Panel_Properties
from sample_panel import Sample_Panel


classes = (
    Sample_Panel_Properties,
    Sample_Panel,
    Sample_Operator,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.sample_panel_properties = bpy.props.PointerProperty(type=Sample_Panel_Properties)


def unregister():
    del bpy.types.Scene.sample_panel_properties
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()