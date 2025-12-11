from PIL import Image, ImageOps, ImageDraw, ImageFont
from io import BytesIO

# logo open
# todo- logo add working rn
# im = Image.open("../images/placeholders/logo.png")
async def banner_1(image_bytes,project_title="Lorem Ip", project_desc="hi", footer="" ):
    im = Image.open(BytesIO(image_bytes))

    crop_size = (80, 80)
    min_size = (160,160)

    # final banner object
    banner_size = (280, 120)
    banner = Image.new("RGBA",banner_size, (0, 0, 0, 0))
    d = ImageDraw.Draw(banner)

    COLORS = {
        # metallics
        "gold":          (255, 215, 0),
        "silver":        (192, 192, 192),
        "bronze":        (205, 127, 50),
        "platinum":      (229, 228, 226),
        "rose_gold":     (183, 110, 121),

        # grayscale
        "white":         (255, 255, 255),
        "black":         (0, 0, 0),
        "light_gray":    (211, 211, 211),
        "gray":          (128, 128, 128),
        "dark_gray":     (64, 64, 64),

        # reds
        "red":           (255, 0, 0),
        "dark_red":      (139, 0, 0),
        "rose":          (255, 102, 102),
        "crimson":       (220, 20, 60),

        # oranges + yellows
        "orange":        (255, 165, 0),
        "dark_orange":   (255, 140, 0),
        "yellow":        (255, 255, 0),
        "amber":         (255, 191, 0),

        # greens
        "green":         (0, 128, 0),
        "light_green":   (144, 238, 144),
        "lime":          (50, 205, 50),
        "mint":          (152, 255, 152),
        "emerald":       (80, 200, 120),

        # blues
        "blue":          (0, 0, 255),
        "sky_blue":      (135, 206, 235),
        "navy":          (0, 0, 128),
        "cyan":          (0, 255, 255),
        "teal":          (0, 128, 128),

        # purples
        "purple":        (128, 0, 128),
        "lavender":      (230, 230, 250),
        "violet":        (238, 130, 238),
        "magenta":       (255, 0, 255),

        # browns / earthy
        "brown":         (150, 75, 0),
        "tan":           (210, 180, 140),
        "sand":          (194, 178, 128),

        # specialty / aesthetic colors
        "pastel_pink":   (255, 182, 193),
        "pastel_blue":   (174, 198, 255),
        "pastel_green":  (119, 221, 119),
        "neon_green":    (57, 255, 20),
        "neon_pink":     (255, 20, 147),
        "neon_blue":     (0, 160, 255)
    }

    # drawing the main body
    # todo- add the color option and smart color picker from logo or some image
    d.rounded_rectangle(
        [(0, 0), banner_size],
        radius=banner_size[1]//20,
        fill=COLORS["bronze"],
        outline=None         
    )

    # drawing the lines
    # todo- border color change!!
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

    banner.paste(im, (20,20), im) # so basically only paste colored pixels no transparent pixels



    # writing the text and description
    # todo- add more fonts and options!
    font_title = ImageFont.truetype("./font/Bitcount.ttf", 20)
    font_desc = ImageFont.truetype("./font/Bitcount.ttf", 8)


    # project_title = str(input())
    # project_desc = str(input())
    # todo - take this from discord input
    # project_title = "Lorem Ip"
    # project_desc = "Lorem Ipsum i72y3r8273 hgu3 g2 t3248y g32847t 23yg 4t2837t 4g238y 4g8237 g4".split(" ")


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
            d.text((120, 40+(count*10)), " ".join(project_desc[prev:i+1]), font=font_desc, fill=(0, 0, 0))
            prev = i
            count+=1

        if i == len(project_desc)-1:
            # i+1 because bro i forgot the part 
            d.text((120, 40+(count*10)), " ".join(project_desc[prev:i+1]), font=font_desc, fill=(0, 0, 0))

        # d.text((120, 50), project_desc[], font=font_desc)

    # todo - discord input or use msg.author!!
    d.text((120, 90), f">>> ${footer}", font=font_desc)

    # banner.show()

    # banner.save("first.png")

    # at the very end of everything
    # todo -  (now adter padding just add gifs and stuff stars and wtv animation)
    pad = 10
    im_padded = ImageOps.expand(banner, border=pad, fill=(0,0,0,0))

    # im_padded.show()
    # im_padded.save("padded.png")
    # return im_padded

    #final output buffer create and send
    output_buffer = BytesIO()
    im_padded.save(output_buffer, format="PNG")

    #seek(0) when opening discord mein
    return output_buffer

if __name__ == "__main__":
    # banner_1(im,"hi", "waddup","hehehe").show()
    print("hi")