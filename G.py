#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Oct 10, 2017 08:25:14 PM
import sys
import numpy as np
import cv2,time
from random import randint
import t
import time
import detect_faces
import Identity
import recognize
import os
import train
try:
    from Tkinter import *
    
except ImportError:
    from tkinter import *

from tkFileDialog import askopenfilename,askdirectory
from PIL import Image,ImageTk,ImageDraw



try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1



def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel_1 (root)
    root.mainloop()

w = None
groupId='123'
key='18a4901b9c644cb9b2a743e1b12aaff4'
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel_1 (w)
    GUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None


def Clea(model,location):
    model.canvas.pack(fill=BOTH, expand=1)
    model.canvas.create_image(79, 0, anchor=NW, image=model.image)   
    paint(model,location)
def paint(model,location):
  a=[]
  if location != 0:
    for i in location:
	#print(i['faceId'])
	#print(point['width'])
	point = i['faceRectangle']
	age = i['faceAttributes']
	
	if i['name'] == 'No Name':
		print("ko co")
		a.append(model.canvas.create_rectangle(point['left']+80, point['top'],point['left']+point['width']+80,point['top']+point['height'],outline='red'))
		model.canvas.create_text(point['left']+65  ,point['top'] - 30,text = i['name'],fill='red',font=("Times New Ronam",20))
		model.canvas.create_text(point['left']+190  ,point['top'] - 30,text = age['age'],fill='red',font=("Times New Ronam",20))
		model.canvas.create_text(point['left']+280  ,point['top'] - 30,text = age['gender'],fill='red',font=("Times New Ronam",20))
	else:		
		model.canvas.create_rectangle(point['left']+80, point['top'],point['left']+point['width']+80,point['top']+point['height'],outline='red')
	#	print(i)
		model.canvas.create_text(point['left']+100  ,point['top'] - 30,text = i['name'],fill='red',font=("Times New Ronam",20))
		model.canvas.create_text(point['left']+180  ,point['top'] - 30,text = age['age'],fill='red',font=("Times New Ronam",20))
		model.canvas.create_text(point['left']+280  ,point['top'] - 30,text = age['gender'],fill='red',font=("Times New Ronam",20))
  else:	
	print(a)
	model.canvas.delete(a)
class New_Toplevel_1:
    path=""
    name=""	
    def Clear(self):
	paint(self,0)
	#self.canvas.delete(ALL)
    def Webcam(self):
	   cap = cv2.VideoCapture(0)
	   while(True):
    		ret, frame = cap.read()
    		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    		cv2.imshow('frame',gray)
    		if cv2.waitKey(1) & 0xFF == ord('q'):
        		break
	   cap.release()
	   fi = t.capture()
	   path = fi
	   print(path)
	   im = Image.open(path)
	   resized = im.resize((700,700),Image.ANTIALIAS)
	   # /home/ngocson/.../***.png
  	   strs = path.split('/')
           nameImageWithDot = strs[len(strs) - 1]
           nameImageWithoutDot = nameImageWithDot.split('.')[0]
 	   newfile = nameImageWithoutDot+'.png'
 	   r = resized.convert('RGB')
           r.save("/home/ngocson/"+newfile)
	   self.image.configure(file="/home/ngocson/"+newfile)
	   self.pathImage = "/home/ngocson/"+newfile

    def Image(self):
	   root=Tk()
	   filee = askopenfilename(initialdir="/home/ngocson")
           im = Image.open(filee)
	   resized = im.resize((700,700),Image.ANTIALIAS)
	   # /home/ngocson/.../***.png
  	   strs = filee.split('/')
           nameImageWithDot = strs[len(strs) - 1]
           nameImageWithoutDot = nameImageWithDot.split('.')[0]
 	   newfile = nameImageWithoutDot+'.png'
 	   r = resized.convert('RGB')
           r.save("/home/ngocson/"+newfile)
	   self.image.configure(file="/home/ngocson/"+newfile)
           self.pathImage = "/home/ngocson/"+newfile
           self.canvas.delete('all')
	   self.canvas.pack(fill=BOTH, expand=1)
           self.canvas.create_image(79, 0, anchor=NW, image=self.image)  
    def Identify(self):
	   #print(self.pathImage)
	   hinh = Image.open(self.pathImage)
	   aa = self.pathImage.split('.')[0]
	   r = hinh.convert('RGB')
	   r.save(aa+'.jpg')
	   faceID =  detect_faces.pathimage(aa+'.jpg')
	   print("Face ID",faceID)	   
	   for i in faceID:		   
	  	personID = Identity.Iden(i['faceId'],groupId,key)
		print("##############",personID)		
		for j in personID:
			if j['candidates'] == []:				
				i['name'] = 'No Name'
			else:			
	   			name = recognize.recog(j['candidates'])	
				if name == None:
				    i['name'] = 'No name'
				else:			
				    i['name'] = name['name']
			print(faceID)

	   Clea(self,faceID)
    def Training(self):
	   filee = askdirectory(initialdir="/home/ngocson/Pictures/Face_Cognitive")
	   train.change(filee)	
    def Quite(self):
        root.quit()

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("598x450+410+100")
        top.title("New Toplevel 1")


	self.image = PhotoImage()
	self.pathImage = ''
	
        self.Frame1 = Label(top,image = self.image)
	self.canvas = Canvas(self.Frame1)
	
        self.Frame1.place(relx=0.02, rely=0.02, relheight=0.97, relwidth=0.63)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(width=375)
		
        self.AddImage = Button(top)
        self.AddImage.place(relx=0.67, rely=0.02, height=36, width=187)
        self.AddImage.configure(activebackground="#d9d9d9")
        self.AddImage.configure(text='''+Image''')
        self.AddImage.configure(width=187)
	self.AddImage.configure(command=self.Image)

	
	
        self.Button3 = Button(top)
        self.Button3.place(relx=0.67, rely=0.11, height=36, width=187)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(text='''Identify''')
        self.Button3.configure(width=187)
	self.Button3.configure(command=self.Identify)
	#self.Button3.configure(command=self.Identif)

        self.Button4 = Button(top)
        self.Button4.place(relx=0.67, rely=0.2, height=36, width=187)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(text='''Clear''')
        self.Button4.configure(width=187)
	self.Button4.configure(command=self.Clear)

        self.Button5 = Button(top)
        self.Button5.place(relx=0.67, rely=0.29, height=36, width=187)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(text='''WebCam''')
        self.Button5.configure(width=187)
	self.Button5.configure(command=self.Webcam)

        self.Button6 = Button(top)
        self.Button6.place(relx=0.67, rely=0.38, height=36, width=187)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(command=self.Quite)
        self.Button6.configure(text='''Quite''')
        self.Button6.configure(width=187)

        self.Button7 = Button(top)
        self.Button7.place(relx=0.69, rely=0.82, height=66, width=177)
        self.Button7.configure(activebackground="#d9d9d9")
        self.Button7.configure(text='''Training''')
        self.Button7.configure(width=177)
	self.Button7.configure(command=self.Training)

if __name__ == '__main__':
    vp_start_gui()


