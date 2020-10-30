import os
import glob
import responsivepathing as rp
from PIL import Image
from datetime import datetime
import gifmanipulation as gm

translator = {
    0:"input",
    1:"set",
    2:"print",
    3:"add1",
    4:"sub1",
    5:"plus1",
    6:"minus1",
    7:"if",
    8:"for",
    9:"comma",
    10:"endline",
    11:"endstatement",
    12:"get"
}

gm.clearcache(False)
gm.extractFrames(rp.here("compiled.gif"), rp.here("cache/"))

def framesToCode(inFolder, outFile):

    global translator

    drakefile = open(rp.here("file.drakeclap"), "w")
    commandidlist = []
    files = glob.glob(rp.here("cache/*"))

    for f in files:
        picture = Image.open(f)
        colorvalue = picture.getpixel((0,0))
        r = colorvalue
        commandidlist.append(r)

    print(datetime.now().strftime("%H:%M:%S"), "Read code from .gif file.")

    for item in commandidlist:
        drakefile.writelines(translator.get(item) + " ")

    print(datetime.now().strftime("%H:%M:%S"), "Translated code to .drakeclap and written to file.")

framesToCode(rp.here("cache/"), rp.here("file.drakeclap"))
