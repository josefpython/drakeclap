from PIL import Image
import os
import glob
import responsivepathing as rp
import string

def extractFrames(inGif, outFolder):

    namelist=[]
    for n in range(26):
        firstletter = string.ascii_lowercase[n]
        for x in range(26):
            secondletter = string.ascii_lowercase[x]
            namelist.append(firstletter + secondletter)

    frame = Image.open(inGif)
    nframes = 0
    while frame:
        frame.save( '%s/%s.gif' % (outFolder, namelist[nframes] ) , 'GIF')
        nframes += 1
        try:
            frame.seek( nframes )
        except EOFError:
            break

    return True

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

    return True