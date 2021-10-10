import bpy
for mat in bpy.data.materials:
    print(mat)
    mat.blend_method = 'HASHED'
    mat.use_backface_culling = True
