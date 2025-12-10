from PIL import Image, ImageOps, ImageDraw

im = Image.open("../images/placeholders/sizes.png")
crop_size = (120, 120)
min_size = (160,160)

# if im.size > min_size:
#     box = (
#         im.size[0]//2 - crop_size[0]//2, 
#         im.size[1]//2 - crop_size[1]//2, 
#         im.size[0]//2 + crop_size[0]//2, 
#         im.size[1]//2 + crop_size[1]//2
#         )
#     region = im.crop(box)
 
# else:
#     region = im

# if im.size > min_size:
#     region = region.rotate(45)
#     im.paste(region, box)
# # im = Image.new("RGBA", (100, 100))

# im.show()

# im = ImageOps.fit(im, crop_size)
# im.thumbnail(crop_size)
# im.show()

im = Image.new("RGBA", (280, 120), (0, 0, 0, 0))
d = ImageDraw.Draw(im)
d.rounded_rectangle(
    [(0, 0), (280, 120)],radius=6,fill=(200, 200, 200),outline=None         
)
# d.rectangle((0, 0, 100, 100), (0, 255, 0, 127))
# d.line((10, 10) + (im.size[0]-10, 10), width=2, fill=(255,255,255))
# d.line((10, 10) + (10, im.size[1]-10), width=2, fill=(255,255,255))
# d.line((10, im.size[1]-10) + (im.size[0]-10, im.size[1]-10), width=2, fill=(255,255,255))
# d.line((im.size[0]-10, im.size[1]-10) + (im.size[0]-10, 10), width=2, fill=(255,255,255))
# # d.line((10, -10) + (10, im.size[1]-10), fill=128)
# # d.line((-10, -10) + (10, im.size[1]-10), fill=128)
# d.circle((10+2,10+2), 2, fill=(255,255,255), outline=None, width=10)
# d.circle((10+2,im.size[1]-10-2), 2, fill=(255,255,255), outline=None, width=1)
# d.circle((im.size[0]-10-2, 10+2), 2, fill=(255,255,255), outline=None, width=1)
# d.circle((im.size[0]-10-2, im.size[1]-10-2), 2, fill=(255,255,255), outline=None, width=1)
# im.show()
d.rounded_rectangle(
    [(11, 11), (280-11, 120-11)],radius=5,outline=(0,0,0), width=1 
)
d.rounded_rectangle(
    [(10, 10), (280-10, 120-10)],radius=5,outline=(255,255,255), width=1      
)
d.rounded_rectangle(
    [(9, 9), (280-9, 120-9)],radius=5,outline=(0,0,0), width=1 
)
pad = 20
im_padded = ImageOps.expand(im, border=pad, fill=(0,0,0,0))

im_padded.show()
# im_padded.save("./test.png")
# from PIL import Image, ImageDraw, ImageFont

# get an image
# with Image.open("Pillow/Tests/images/hopper.png").convert("RGBA") as base:

#     # make a blank image for the text, initialized to transparent text color
#     txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

#     # get a font
#     fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
#     # get a drawing context
#     d = ImageDraw.Draw(txt)

#     # draw text, half opacity
#     d.text((10, 10), "Hello", font=fnt, fill=(255, 255, 255, 128))
#     # draw text, full opacity
#     d.text((10, 60), "World", font=fnt, fill=(255, 255, 255, 255))

#     out = Image.alpha_composite(base, txt)

#     out.show()


