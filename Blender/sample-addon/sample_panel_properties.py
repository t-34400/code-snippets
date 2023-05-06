import bpy


class Sample_Panel_Properties(bpy.types.PropertyGroup):
    sample_prop_tag = "sample_prop"

    def get_sample_list(self, context):
        return ["Apple", "Banana", "Cooke"]


    sample_prop: bpy.props.EnumProperty(
        name=sample_prop_tag,
        items=get_sample_list,
        description="Sample property",
    )