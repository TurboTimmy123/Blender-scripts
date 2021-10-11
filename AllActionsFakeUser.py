# Blender only saves actions that are associated with an armature
# If an action doesn't belong to anything it will be deleted on exit 
# This can can prevented if it's labelled as a fake user

import bpy

for a in bpy.data.actions:
    print('Locking', a)
    bpy.data.actions[a.name].use_fake_user = True