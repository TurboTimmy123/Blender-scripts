# If an action begins with a certain string, prepend it with something else
# Useful when dealing with duplicate names to categorize them 

import bpy

for a in bpy.data.actions:
    if a.name.startswith('Anim'):
        print('Renaming', a.name)
        a.name = "01_" + a.name
        print(a.name)