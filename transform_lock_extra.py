bl_info = {
    "name": "Transform Locks Extra",
    "description": "Adds toggle button in property region for enabling lock transform to all selected object",
    "author": "Aditia A. Pratama",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "3D View > Property Region (N-key)",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "3D View",
}

import bpy

## Operator ## 
class locZ_lock(bpy.types.Operator):
    'Location Z Lock'
    bl_idname='locz.toggle'
    bl_label='Lock Loc Z'     
    
    def execute(self, context):
        sel = bpy.context.selected_objects
        for obj in sel:
            try:
                if obj.lock_location[2] == True:
                    obj.lock_location[2] = False
                else:
                    obj.lock_location[2] = True
            except KeyError:
                print ("No lock identified")
        return {'FINISHED'}

class locY_lock(bpy.types.Operator):
    'Location Y Lock'
    bl_idname='locy.toggle'
    bl_label='Lock Loc Y'     
    
    def execute(self, context):
        sel = bpy.context.selected_objects
        for obj in sel:
            try:
                if obj.lock_location[1] == True:
                    obj.lock_location[1] = False
                else:
                    obj.lock_location[1] = True
            except KeyError:
                print ("No lock identified")
        return {'FINISHED'}
    
class locX_lock(bpy.types.Operator):
    'Location X Lock'
    bl_idname='locx.toggle'
    bl_label='Lock Loc X'     
    
    def execute(self, context):
        sel = bpy.context.selected_objects
        for obj in sel:
            try:
                if obj.lock_location[0] == True:
                    obj.lock_location[0] = False
                else:
                    obj.lock_location[0] = True
            except KeyError:
                print ("No lock identified")
        return {'FINISHED'}
    
class rotZ_lock(bpy.types.Operator):
    'Rotation Z Lock'
    bl_idname='rotz.toggle'
    bl_label='Lock Rot Z'     
    
    def execute(self, context):
        sel = bpy.context.selected_objects
        for obj in sel:
            try:
                if obj.lock_rotation[2] == True:
                    obj.lock_rotation[2] = False
                else:
                    obj.lock_rotation[2] = True
            except KeyError:
                print ("No lock identified")
        return {'FINISHED'}

class rotY_lock(bpy.types.Operator):
    'Rotation Y Lock'
    bl_idname='roty.toggle'
    bl_label='Lock Rot Y'     
    
    def execute(self, context):
        sel = bpy.context.selected_objects
        for obj in sel:
            try:
                if obj.lock_rotation[1] == True:
                    obj.lock_rotation[1] = False
                else:
                    obj.lock_rotation[1] = True
            except KeyError:
                print ("No lock identified")
        return {'FINISHED'}
    
class rotX_lock(bpy.types.Operator):
    'Rotation X Lock'
    bl_idname='rotx.toggle'
    bl_label='Lock Rot X'     
    
    def execute(self, context):
        sel = bpy.context.selected_objects
        for obj in sel:
            try:
                if obj.lock_rotation[0] == True:
                    obj.lock_rotation[0] = False
                else:
                    obj.lock_rotation[0] = True
            except KeyError:
                print ("No lock identified")
        return {'FINISHED'}
    
class scaleZ_lock(bpy.types.Operator):
    'Scale Z Lock'
    bl_idname='scalez.toggle'
    bl_label='Lock scale Z'     
    
    def execute(self, context):
        sel = bpy.context.selected_objects
        for obj in sel:
            try:
                if obj.lock_scale[2] == True:
                    obj.lock_scale[2] = False
                else:
                    obj.lock_scale[2] = True
            except KeyError:
                print ("No lock identified")
        return {'FINISHED'}
    
class scaleY_lock(bpy.types.Operator):
    'Scale Y Lock'
    bl_idname='scaley.toggle'
    bl_label='Lock scale Y'     
    
    def execute(self, context):
        sel = bpy.context.selected_objects
        for obj in sel:
            try:
                if obj.lock_scale[1] == True:
                    obj.lock_scale[1] = False
                else:
                    obj.lock_scale[1] = True
            except KeyError:
                print ("No lock identified")
        return {'FINISHED'}
 
class scaleX_lock(bpy.types.Operator):
    'Scale X Lock'
    bl_idname='scalex.toggle'
    bl_label='Lock scale X'     
    
    def execute(self, context):
        sel = bpy.context.selected_objects
        for obj in sel:
            try:
                if obj.lock_scale[0] == True:
                    obj.lock_scale[0] = False
                else:
                    obj.lock_scale[0] = True
            except KeyError:
                print ("No lock identified")
        return {'FINISHED'}
    
## UI ##

class TransformLockExtra(bpy.types.Panel):
    bl_label = "Transform Locks Extra"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"
       
    def draw(self, context):
        layout = self.layout
        
        col = layout.column()
        col.label(text="Lock Location All: ")
        
        split = col.split()
        row = split.row(align=True)
        row.operator("locx.toggle", text="X")
        row.operator("locy.toggle", text="Y")
        row.operator("locz.toggle", text="Z")
        
        col.label(text="Lock Rotation All: ")
        
        split = col.split()
        row = split.row(align=True)
        row.operator("rotx.toggle", text="X")
        row.operator("roty.toggle", text="Y")
        row.operator("rotz.toggle", text="Z")
        
        col.label(text="Lock Scale All: ")
        
        split = col.split()
        row = split.row(align=True)
        row.operator("scalex.toggle", text="X")
        row.operator("scaley.toggle", text="Y")
        row.operator("scalez.toggle", text="Z")

classes = (
    locX_lock,
    locY_lock,
    locZ_lock,
    rotX_lock,
    rotY_lock,
    rotZ_lock,
    scaleX_lock,
    scaleY_lock,
    scaleZ_lock,
    TransformLockExtra
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
