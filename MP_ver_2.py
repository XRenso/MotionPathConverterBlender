import bpy
bl_info = {'name' : 'Motion Path to Curve', 'category' : 'Converter', 'author': 'XRenso'}







class AllObjects(bpy.types.Operator):
    bl_idname = "object.convert_motion_path_every"
    bl_label = "Convert all objects"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self,context):            
        obj = bpy.data.objects
        for ob in obj: 
            mp = ob.motion_path
            if mp:
                path = bpy.data.curves.new('path','CURVE')
                curve = bpy.data.objects.new(ob.name + '_path',path)
                context.scene.collection.objects.link(curve)
                path.dimensions = '3D'
                spline = path.splines.new('BEZIER')
                spline.bezier_points.add(len(mp.points)-1)
                for i,o in enumerate(spline.bezier_points):
                    o.co = mp.points[i].co
                    o.handle_right_type = 'AUTO'
                    o.handle_left_type = 'AUTO'    
        return {'FINISHED'}


class SellObjects(bpy.types.Operator):
    bl_idname = "object.convert_motion_path_sellected"
    bl_label = "Convert only selected objects"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self,context):            
        obj = bpy.context.selected_objects
        for ob in obj: 
            mp = ob.motion_path
            if mp:
                path = bpy.data.curves.new('path','CURVE')
                curve = bpy.data.objects.new(ob.name + '_path',path)
                context.scene.collection.objects.link(curve)
                path.dimensions = '3D'
                spline = path.splines.new('BEZIER')
                spline.bezier_points.add(len(mp.points)-1)
                for i,o in enumerate(spline.bezier_points):
                    o.co = mp.points[i].co
                    o.handle_right_type = 'AUTO'
                    o.handle_left_type = 'AUTO'    
        return {'FINISHED'}


class Converter(bpy.types.Panel):
    bl_label = "Convert Motion Path to Curve"
    bl_idname = "SCENE_PT_converter_paths"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
       
        layout = self.layout.column()
        
        scene = context.scene
        
        row = layout.row()
        row.scale_y = 1.5
        row.operator("object.convert_motion_path_every")
        row = layout.row()
        row.scale_y = 1.5
        row.operator("object.convert_motion_path_sellected")
        




def register():
    bpy.utils.register_class(SellObjects)
    bpy.utils.register_class(AllObjects)
    bpy.utils.register_class(Converter)


def unregister():
    bpy.utils.unregister_class(SellObjects)
    bpy.utils.unregister_class(AllObjects)
    bpy.utils.unregister_class(Converter)



if __name__ == "__main__":
    register()
