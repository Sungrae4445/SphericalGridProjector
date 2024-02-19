#Released under GPL 3.0 License
#Copyright 2024 Sungrae Kim


import bpy


def main(context):
    ob = context.active_object
    for vertex in ob.data.vertices:
        vertex.co.z = (1-pow(vertex.co.x,4))*(1-pow(vertex.co.y,4))


class InitialGrid(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.initialgrid_operator"
    bl_label = "Initial Grid Operator"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(InitialGrid.bl_idname, text=InitialGrid.bl_label)


# Register and add to the "object" menu (required to also use F3 search "Simple Object Operator" for quick access).
def register():
    bpy.utils.register_class(InitialGrid)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(InitialGrid)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.object.initialgrid_operator()
