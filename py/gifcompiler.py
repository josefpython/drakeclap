from PIL import Image
import responsivepathing as rp
from distutils.dir_util import copy_tree

translator = {
    "input":0,
    "set":1,
    "print":2,
    "add1":3,
    "sub1":4,
    "plus1":5,
    "minus1":6,
    "if":7,
    "for":8,
    "comma":9,
    "endline":10,
    "endstatement":11,
    "get":12
}

string_input = input() #TODO

totranslate = string_input.split(" ")
images = []
imdex = 0
copy_tree(rp.here("static/clap_frames"), rp.here("cache"))

for item in totranslate:

    print(item)
    path = rp.here("cache/"+ str(imdex) +".png")
    picture = Image.open(path)
    picture_rgb = picture.convert("RGB")
    r,g,b = picture_rgb.getpixel((0,0))
    picture_rgb.putpixel((0,0),(translator.get(item),g,b))
    picture_rgb.save(path)

    if imdex == 29:
        imdex = 0