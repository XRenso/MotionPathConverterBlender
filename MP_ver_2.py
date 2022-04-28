import bpy
bl_info = {'name' : 'Motion Path to Curve', 'category' : 'Converter', 'author': 'XRenso'}

name_of_primitive = ''


def get_enum_value(self, context):
    global name_of_primitive
    j = self.object
    name_of_primitive = j
    print(name_of_primitive)

mode_options = [
        ("mesh.primitive_plane_add", "Plane", '', 'MESH_PLANE', 0),
        ("mesh.primitive_cube_add", "Cube", '', 'MESH_CUBE', 1),
        ("mesh.primitive_circle_add", "Circle", '', 'MESH_CIRCLE', 2),
        ("mesh.primitive_uv_sphere_add", "UV Sphere", '', 'MESH_UVSPHERE', 3),
        ("mesh.primitive_ico_sphere_add", "Ico Sphere", '', 'MESH_ICOSPHERE', 4),
        ("mesh.primitive_cylinder_add", "Cylinder", '', 'MESH_CYLINDER', 5),
        ("mesh.primitive_cone_add", "Cone", '', 'MESH_CONE', 6),
        ("mesh.primitive_torus_add", "Torus", '', 'MESH_TORUS', 7)
    ]

PROPS = [
    ('add_object', bpy.props.BoolProperty(name='Add Object', default=False)),
    ('object', bpy.props.EnumProperty(name='Premetives', description = 'Premetives object for add on curve', items = mode_options,default="mesh.primitive_plane_add", update=get_enum_value)),
]




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
        for (prop_name, _) in PROPS:
            col = layout.column()
            col.scale_y = 1.5
            col.prop(context.scene, prop_name)




def register():
    bpy.utils.register_class(SellObjects)
    bpy.utils.register_class(AllObjects)
    bpy.utils.register_class(Converter)
    for (prop_name, prop_value) in PROPS:
        setattr(bpy.types.Scene, prop_name, prop_value)

def unregister():
    bpy.utils.unregister_class(SellObjects)
    bpy.utils.unregister_class(AllObjects)
    bpy.utils.unregister_class(Converter)
    for (prop_name, prop_value) in PROPS:
        delattr(bpy.types.Scene, prop_name, prop_value)


register()    
    
if __name__ == "__main__":
    register()
