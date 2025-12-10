from PIL import Image, ImageOps, ImageDraw, ImageFont


# logo open
# todo- logo add working rn
im = Image.open("../images/placeholders/logo.png")
crop_size = (80, 80)
min_size = (160,160)

# final banner object
banner_size = (280, 120)
banner = Image.new("RGBA",banner_size, (0, 0, 0, 0))
d = ImageDraw.Draw(banner)


# drawing the main body
# todo- add the color option and smart color picker from logo or some image
d.rounded_rectangle(
    [(0, 0), banner_size],
    radius=banner_size[1]//20,
    fill=(200, 200, 200),
    outline=None         
)


# drawing the lines
d.rounded_rectangle(
    [(11, 11), (banner_size[0]-11, banner_size[1]-11)],
    radius=banner_size[1]//24,
    outline=(0,0,0),
    width=banner_size[1]//120
)

d.rounded_rectangle(
    [(10, 10), (banner_size[0]-10, banner_size[1]-10)],
    radius=banner_size[1]//24,
    outline=(255,255,255),
    width=banner_size[1]//120
)

d.rounded_rectangle(
    [(9, 9), (banner_size[0]-9, banner_size[1]-9)],
    radius=banner_size[1]//24,
    outline=(0,0,0),
    width=banner_size[1]//120
)


# pasting the logo
im = ImageOps.fit(im, crop_size)

banner.paste(im, (20,20))


# writing the text and description
# todo- add more fonts and options!
font_title = ImageFont.truetype("./font/Bitcount.ttf", 20)
font_desc = ImageFont.truetype("./font/Bitcount.ttf", 8)


# project_title = str(input())
# project_desc = str(input())
# todo - take this from discord input
project_title = "Lorem Ip"
project_desc = "Lorem Ipsum i72y3r8273 hgu3 g2 t3248y g32847t 23yg 4t2837t 4g238y 4g8237 g4".split(" ")


# todo - smart font color or just discord input!
d.text((120, 18), project_title, font=font_title, fill=(0, 0, 0))

line_len = 0
prev = 0
count=0
for i in range(len(project_desc)):
    line_len+=len(project_desc[i])*8 # this variable changes with font rememeber so make list with mapping of diff fonts 
    # todo - the comment right above this one 
    if line_len > 120:
        line_len = 0
        d.text((120, 40+(count*10)), " ".join(project_desc[prev:i]), font=font_desc, fill=(0, 0, 0))
        prev = i
        count+=1

    if i == len(project_desc)-1:
        d.text((120, 40+(count*10)), " ".join(project_desc[prev:i]), font=font_desc, fill=(0, 0, 0))

    # d.text((120, 50), project_desc[], font=font_desc)

# todo - discord input or use msg.author!!
d.text((120, 90), ">>> $username", font=font_desc)

# banner.show()

# banner.save("first.png")

# at the very end of everything
# todo -  (now adter padding just add gifs and stuff stars and wtv animation)
pad = 10
im_padded = ImageOps.expand(banner, border=pad, fill=(0,0,0,0))

im_padded.show()
im_padded.save("padded.png")
