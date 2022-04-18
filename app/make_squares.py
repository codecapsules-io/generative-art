from PIL import Image, ImageDraw, ImageFont
import base64
import random
import json
import io

pallets = []
with open("pallets.json") as f:
    ps = json.load(f)
    for p in ps:
        pallet = [tuple(x) for x in p]
        pallets.append(pallet)

BLACK = (0, 0, 0, 255)

def create():
    img = Image.new("RGBA", (1000, 1000), (255, 255, 255, 255))
    d = ImageDraw.Draw(img)


    num_recs = random.randrange(20, 40)
    min_size = random.randrange(20,50)
    max_size = min_size + random.randrange(20,100)
    colors = random.choice(pallets)
    stroke_width = random.randrange(1,5)
    xoffset = 0
    yoffset = 0
    for row in range(num_recs):
        for rec in range(num_recs):
            topleftx = random.randrange(0, 50) + xoffset
            toplefty = random.randrange(0, 50) + yoffset
            bottomrightx = topleftx + random.randrange(min_size,max_size)
            bottomrighty = toplefty + random.randrange(min_size,max_size)
            color = random.choice(colors)
            xoffset += 50
            r = d.rectangle([topleftx, toplefty, bottomrightx, bottomrighty], fill=color, outline=BLACK, width=stroke_width)
        yoffset += 50
        xoffset = 0
    #img.save(outname)
    image = io.BytesIO()
    img.save(image, "PNG")
    image.seek(0)
    img_b64 = base64.b64encode(image.getvalue()).decode()
    return img_b64
    
#for i in range(10):
#    create(f"image{i}.png")
