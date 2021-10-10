# Must be in edit mode

import bpy
for bone in bpy.context.selected_editable_bones[:]:
    bone.name += '.L'
    print(bone.name)
