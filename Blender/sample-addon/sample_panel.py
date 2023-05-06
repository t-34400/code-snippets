import bpy
import Sample_Panel_Properties
import Sample_Operator

class Sample_Panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_sample_panel"
    bl_label = "Sample panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Sample Panel Tab"

    def draw(self, context):
        layout = self.layout
        props = context.scene.sample_panel_properties

        row = layout.row()
        row.label(text="")
        row.prop(props, Sample_Panel_Properties.sample_prop_tag, text="")

        layout.separator()

        layout.operator(Sample_Operator.bl_idname, text="Click here!")
