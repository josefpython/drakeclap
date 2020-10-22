import os
import glob
import responsivepathing as rp
from PIL import Image
from datetime import datetime

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

def clearcache(forced):

    files = glob.glob(rp.here("cache/*"))
    if len(files) > 0:
        if forced == False:
            ans = input("Files were found in the cache folder. These have to be removed before proceeding. Do you wish to continue? y/n ").upper()
            if ans == "Y":
                for f in files:
                    os.remove(f)
            else:
                exit()
        else:
            for f in files:
                os.remove(f)

    print(datetime.now().strftime("%H:%M:%S"), "Cleared cache folder.")

def extractFrames(inGif, outFolder):
    frame = Image.open(inGif)
    nframes = 0
    while frame:
        frame.save( '%s/%s.png' % (outFolder, nframes ) , 'PNG')
        nframes += 1
        try:
            frame.seek( nframes )
        except EOFError:
            break

    print(datetime.now().strftime("%H:%M:%S"), "Loaded .gif file into cache folder.")
    return True

def framesToCode(inFolder, outFile):

    global translator

    drakefile = open(rp.here("file.drakeclap"), "w")
    commandidlist = []
    files = glob.glob(rp.here("cache/*"))

    for f in files:
        picture = Image.open(f)
        picture_rgb = picture.convert("RGB")
        colorvalue = picture_rgb.getpixel((0,0))
        r = colorvalue[0]
        commandidlist.append(r)

    print(datetime.now().strftime("%H:%M:%S"), "Read code from .gif file.")

    for item in commandidlist:
        drakefile.writelines(" " + str(item) + " ")

    print(datetime.now().strftime("%H:%M:%S"), "Translated code to .drakeclap and written to file.")

#clearcache(False)
#extractFrames(rp.here("static/clap.gif"), rp.here("cache/"))
framesToCode(rp.here("cache/"), rp.here("file.drakeclap"))
#clearcache(True)

print(datetime.now().strftime("%H:%M:%S"), "Launching .drakefile to .py decoder.")
#TODO LAUNCH DECODER
print(datetime.now().strftime("%H:%M:%S"), "Decoder expected to have finished, launching runtime.py")
#TODO LAUNCH RUNTIME