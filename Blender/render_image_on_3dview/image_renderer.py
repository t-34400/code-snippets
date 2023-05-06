import bpy
import bgl
import gpu
from gpu_extras.batch import batch_for_shader


class Image_Renderer:

    def __init__(self):
        self.shader = gpu.shader.from_builtin('2D_IMAGE')


    def set_image_bottom_left(self, image, target_width):
        img_width = image.size[0]
        img_height = image.size[1]

        area_width = self.get_area_width()
        if area_width == 0:
            return

        margin_bottom = 20
        margin_right = 60

        display_width = min(target_width, area_width - margin_right * 2)
        display_height = int(img_height * (display_width / img_width))

        pos = (
                (area_width - margin_right - display_width, margin_bottom), 
                (area_width - margin_right - display_width, display_height + margin_bottom), 
                (area_width - margin_right, margin_bottom), 
                (area_width - margin_right, display_height + margin_bottom)
            )
        self.batch = batch_for_shader(self.shader, 'TRI_STRIP', {
            "pos": pos,
            "texCoord": ((0, 0), (0, 1), (1, 0), (1, 1)),
        })

        self.texture = gpu.texture.from_image(image)

        if image.gl_load():
            raise Exception()
        

    def get_area_width(self):
        if not hasattr(bpy.context, "screen"):
            return 0
        
        view3ds = [area for area in bpy.context.screen.areas if area.type == 'VIEW_3D']
        windows = sum([[region for region in view3d.regions if region.type  == 'WINDOW'] for view3d in view3ds], [])

        return max([window.width for window in windows] + [0])


    def draw_callback(self):
        if hasattr(self, "texture"):
            gpu.state.blend_set("ALPHA")
            self.shader.bind()
            self.shader.uniform_sampler("image", self.texture)
            self.batch.draw(self.shader)
            gpu.state.blend_set("NONE")
