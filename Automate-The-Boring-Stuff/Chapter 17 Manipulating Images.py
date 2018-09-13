"""
Automate The Boring Stuff Chapter 17
Manipulating Images
Github: MattDWe
"""

import os
from PIL import ImageColor, Image, ImageDraw, ImageFont

print(ImageColor.getcolor("red", "RGBA"))

os.chdir(".\\Chapter 17")
catIm = Image.open("zophie.png")
print(catIm.size)
width, height = catIm.size
print(width)
print(height)
print(catIm.filename)
print(catIm.format)
print(catIm.format_description)
catIm.save("zophie.jpg")

im = Image.new("RGBA", (100, 200), "purple")
im.save("purpleImage.png")
im2 = Image.new("RGBA", (20, 20))
im2.save("transparentImage.png")

croppedIm = catIm.crop((335, 245, 565, 560))
croppedIm.save("cropped.png")

catIm = Image.open("zophie.png")
catCopyIm = catIm.copy()

faceIm = catIm.crop((335, 345, 565, 560))
catCopyIm.paste(faceIm, (0,0))
catCopyIm.save("pasted.png")

catImWidth, catImHeight = catIm.size
faceImWidth, faceImHeight = faceIm.size
catCopyTwo = catIm.copy()
for left in range(0, catImHeight, faceImHeight):
    for top in range(0, catImHeight, faceImHeight):
        print(left, top)
        catCopyTwo.paste(faceIm, (left, top))
catCopyTwo.save("titled.png")

width, height = catIm.size
quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
quartersizedIm.save("quartersized.png")
svelteIm = catIm.resize((width, height + 300))
svelteIm.save("svelte.png")

catIm.rotate(90).save("rotated90.png")
catIm.rotate(6, expand=True).save("rotated6_expanded.png")
catIm.transpose(Image.FLIP_LEFT_RIGHT).save("horizontal_flip.png")

im = Image.new("RGBA", (100, 100))
im.getpixel((0, 0))
for x in range(100):
    for y in range(50):
        im.putpixel((x, y), (210, 210, 210))
for x in range(100):
    for y in range(50, 100):
        im.putpixel((x, y), ImageColor.getcolor("darkgray", "RGBA"))
im.save("putPixel.png")

im = Image.new("RGBA", (200, 200), "white")
draw = ImageDraw.Draw(im)
draw.line([(0,0), (199, 0), (199, 199), (0, 199), (0, 0)], fill="black")
draw.rectangle((20, 30, 60, 60), fill="blue")
draw.ellipse((120, 30, 160, 60), fill="red")
draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill="brown")
for i in range(100, 200, 10):
    draw.line([(i, 0), (200, i - 100)], fill="green")
im.save("drawing.png")

im = Image.new("RGBA", (200, 200), "white")
draw = ImageDraw.Draw(im)
draw.text((20, 150), "Hello", fill="purple")
im.save("text.png")

"""
Practice Questions
1. red, green, blue, alpha
2. ImageColor.getcolor("CornflowerBlue", "RGBA")
3. x and y where y is negative
4. Image.open("zophie.png")
5. imageObj.size
6. imageObj.crop((0, 50, 50, 50))
7. ImageObj.save("name.png")
8. ImageDraw
9. ImageDraw.Draw()
"""
