# Must be in pose mode

import bpy
for bone in bpy.context.object.data.bones[:]:
    bone.bbone_segments = 4
    print(bone.name)
