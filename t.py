import numpy as np
import cv2,time
from random import randint

def capture():
	
	ramp = 1
	
	came = cv2.VideoCapture(0)
	
	def get_image():
	 	retval, im = came.read()
 	 	return im
	for i in xrange(ramp):
 	 	temp = get_image()
		gray = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
    		cv2.imshow('temp',gray)
	 	print("Taking image...")
	 	a = randint(100,999)
		
	 	camera_capture = get_image()
		time.sleep(5)
	 	file = "/home/ngocson/{0}.png".format(a)
	 
	 	cv2.imwrite(file, camera_capture)
 		return file
	

