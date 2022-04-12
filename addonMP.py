import bpy
bl_info = {'name' : 'MotionPathToCurve', 'category' : 'Converter', 'author': 'XRenso'}


class MotionPathToCurve(bpy.types.Operator):
    bl_idname = "object.convert_motion_path"
    bl_label = "Convert Motion Path to Curve"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        ob = bpy.context.object
        mp = ob.motion_path
        if mp:
            path = bpy.data.curves.new('path','CURVE')
            curve = bpy.data.objects.new('Curve',path)
            context.scene.collection.objects.link(curve)
            path.dimensions = '3D'
            spline = path.splines.new('BEZIER')
            spline.bezier_points.add(len(mp.points)-1)
            for i,o in enumerate(spline.bezier_points):
                o.co = mp.points[i].co
                o.handle_right_type = 'AUTO'
                o.handle_left_type = 'AUTO'

            return {'FINISHED'}

def menu_func(self,context):
    self.layout.operator(MotionPathToCurve.bl_idname)

def register():
    bpy.utils.register_class(MotionPathToCurve)
    bpy.types.VIEW3D_MT_object.append(menu_func)
def unregister():
    bpy.utils.unregister_class(MotionPathToCurve)

register()

if __name__ == "__main__":
    register()
