#for screen capturing library pillow
from PIL import ImageGrab
#for coverting into array........numpy
import numpy as np
#for Python bindings designed to solve computer vision problems.......cv2
import cv2
#for screen resolution finding........win32api
from win32api import GetSystemMetrics
#system resolution 
import datetime
width=GetSystemMetrics(0)
hieght=GetSystemMetrics(1)
time_stamp=datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'
fourcc=cv2.VideoWriter_fourcc('m','p','4','v')
captured_video=cv2.VideoWriter(file_name,fourcc,20.0,(width,hieght))

webcam=cv2.VideoCapture(0)

while True:
    img=ImageGrab.grab(bbox=(0,0,1366,768))
    img_np=np.array(img)
    img_final=cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    _,frame=webcam.read()
    fr_hieght,fr_width, _ = frame.shape
    img_final[0:fr_hieght,0:fr_width,:] = frame[0:fr_hieght,0:fr_width, :]
    cv2.imshow('Secret Capture',img_final)
    #cv2.imshow('webcam',frame)
    captured_video.write(img_final)
    if cv2.waitKey(10)==ord('q'):
        break