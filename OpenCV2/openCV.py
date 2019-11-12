
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:57:45 2019

@author: ravkumar
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt
import os
import sys 
from termcolor import colored, cprint 
import ctypes



# Read first image
unmarked_set = os.getcwd() + "/images/Unmarked_set/"
marked_set = os.getcwd() + "/images/marked_set/"
img_1 = cv2.imread(unmarked_set + "img-1.jpg")
resize = img_1
	#get the size of image
resize = cv2.resize(img_1,(int(img_1.shape[1]/2),int(img_1.shape[0]/2)))
#resize = cv2.resize(img_1,(1920,1080))
	#passed positon of the rectangle shape
cv2.rectangle(resize,(893,507),(773,327),(0,0,255),3)
cv2.rectangle(resize, (737,634),(885,761), (0, 0, 255), 3) 
cv2.rectangle(resize, (1476,420),(1846,894), (0, 0, 255), 3) 

# save image 1
cv2.imwrite(marked_set + "1.jpg",resize)

# read secound image

loadImg_2 = cv2.imread(unmarked_set + "img-2.jpg")
img2 = loadImg_2

cv2.rectangle(loadImg_2,(803,786),(1141,1122),(0,0,255),3)
cv2.rectangle(loadImg_2, (1025,468),(1193,631), (0, 0, 255), 5)
cv2.imwrite(marked_set + "2.jpg",loadImg_2)

# read third image

loadImg_3 = cv2.imread(unmarked_set + "img-3.jpg")
img3 = loadImg_3
resize = cv2.resize(img3,(1920,1080))
cv2.rectangle(loadImg_3,(774,617),(1005,795),(0,0,255),3)
cv2.rectangle(loadImg_3,(1100,563),(1278,751), (0, 0, 255), 3)
cv2.imwrite(marked_set + "3.jpg",loadImg_3)    
updatemsg = colored("Images has saved in marked folder. Please verified.",
                    'red')
ctypes.windll.user32.MessageBoxW(0, "Images has saved in marked folder. Please verified.",
                                 "Information", 1)

