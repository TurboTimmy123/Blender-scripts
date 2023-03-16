# Converts MHR NRRT textures into OpenGL Normal maps with +45 degree rotation fix
# Usage: python NRRT_to_NM.py [NRRT path]
# Requires Python Imaging Library
# pip install Pillow

import sys
from PIL import Image 

R = 0.7071067811865476 # sin(45), cos(45), sqrt(1/2)
def RotateVec45(x, y):
    qx = (R * x) - (R * y)
    qy = (R * x) + (R * y)
    return [qx, qy]

name = sys.argv[1]
img = Image.open(name)
newim = Image.new(mode="RGBA", size=(img.width, img.height))

for px in range(img.width):
    if px % 100 == 0: print(str(px) + "/" + str(img.width), end='\r', flush=True)
    for py in range(img.height):
        a = img.getpixel((px,py))
        rot = RotateVec45(a[1]-127, (a[3]-127)) # NM data sits in Green/Alpha channels
        newim.putpixel((px, py), (int(rot[1] + 127), int(rot[0] + 127), 255))

newName = name[:name.rfind("_NRRT")] + "_NM.PNG"
newim.save(newName, "PNG")
print("Velkhana best monster")
