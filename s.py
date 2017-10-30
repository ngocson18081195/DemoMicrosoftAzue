import sys
import Image, ImageDraw, datetime
import opencv
#this is important for capturing/displaying images
from opencv import highgui

camera = highgui.cvCreateCameraCapture(0)
def get_image():
    for i in range(10):
            im = highgui.cvQueryFrame(camera)
    # Add the line below if you need it (Ubuntu 8.04+)
    #im = opencv.cvGetMat(im)
    #convert Ipl image to PIL image
    return opencv.adaptors.Ipl2PIL(im)

im = get_image()
draw = ImageDraw.Draw(im)
now = datetime.datetime.now()
draw.text((10,10), str(now))
im.save('/home/ngocson/webcam/img/home.png', "PNG")
