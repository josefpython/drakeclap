from PIL import Image
import responsivepathing as rp
from distutils.dir_util import copy_tree
from datetime import datetime
import string
import gifmanipulation as gm
import glob

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
start = ord('a') - 1

gm.clearcache(False)
gm.extractFrames(rp.here("static/clap.gif"), rp.here("cache/"))


def compiletogif():
    totranslate = string_input.split(" ")
    files = glob.glob(rp.here("cache/*"))
    x=0
    images = []

    for item in totranslate:
        f = files[x]

        picture = Image.open(f)
        picval = picture.getpixel((0,0))
        picture.putpixel((0,0), translator.get(item))
        images.append(picture)
        x=x+1

        print("Adding", translator.get(item), "to", f)

        if x == 29:
            x = 0

    images[0].save(rp.here("compiled.gif"), save_all=True, append_images=images[1:], optimize=True, loop=0)



compiletogif()    

def notworking():


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
