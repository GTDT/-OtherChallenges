#:1 Video to pictures converter

import ctypes

frame = 1

FrameNumber = str(frame)


directory = "C:\CuratedWallpaper" + "\\"
imagename = "000"
imageformat = ".png"
imagePath = directory + imagename + FrameText + imageformat

def changeBG(imagePath):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, imagePath, 3)
    print(imagePath,'\n',FrameNumber)


while frame < 21:
    changeBG(imagePath)
    frame += 1
    FrameText = str(frame)
    imagePath = directory + imagename + FrameText + imageformat
    if frame == 20:
        frame -= 20