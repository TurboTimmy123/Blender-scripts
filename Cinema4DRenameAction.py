# Any FBX with animations exported from Cinema 4D will be imported to blender
# with the actions called 'CINEMA_4D_Main', even if the file is saved as something else
# This simply replaces the name of the animation as seen in Blender with the name of the file

import os

for filename in os.listdir('.'):
    if filename.endswith(".fbx"):
        print()
        name = filename.replace(" ", "")
        name = name.replace(".fbx", "")
        # Cannot increase size of binary file, must match original animation name
        name = name.ljust(14)[:14]

        print(filename)
        print('<'+name+'>')
        f = open(filename, "rb")
        data = f.read()
        print('Replacing')
        data = data.replace(b"CINEMA_4D_Main", name.encode())
        with open('fix_'+name.replace(" ","")+'.fbx', "wb") as output_file:
            output_file.write(data)
            output_file.close()
        f.close()
        continue
    else:
        continue