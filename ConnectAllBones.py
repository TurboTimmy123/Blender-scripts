# Must be in edit mode

import bpy
for bone in bpy.context.active_object.data.edit_bones[:]:
    bone.use_connect = True
