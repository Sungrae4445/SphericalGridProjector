#Released under GPL 3.0 License
#Copyright 2024 Sungrae Kim

import bpy
from mathutils import *

def main(context):
    ob = context.active_object
    for vertex in ob.data.vertices:
        vertex_co = Vector((vertex.co.x,vertex.co.y,vertex.co.z))
        vertex_co.normalize()
        
        #radius
        radius_scalar = 100
        
        vertex.co.x = vertex_co[0]*radius_scalar
        vertex.co.y = vertex_co[1]*radius_scalar
        vertex.co.z = vertex_co[2]*radius_scalar
        
class SphericalGrid(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.sphericalgrid_operator"
    bl_label = "Spherical Grid Operator"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(InitialGrid.bl_idname, text=SphericalGrid.bl_label)


# Register and add to the "object" menu (required to also use F3 search "Simple Object Operator" for quick access).
def register():
    bpy.utils.register_class(SphericalGrid)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(SphericalGrid)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.object.sphericalgrid_operator()
