import sys
import os
import cv2
import numpy as np
from tqdm import tqdm

fgdir = sys.argv[1]
outdir = fgdir + "_hue"

os.mkdir(outdir)


def mouseRGB(event,x,y,flags,param):
	if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
		colorsB = param[y,x]
		colorsG = param[y,x]
		colorsR = param[y,x]
		colors  = param[y,x]
		print("Red: ",colorsR)
		print("Green: ",colorsG)
		print("Blue: ",colorsB)
		print("BRG Format: ",colors)
		print("Coordinates of pixel: X: ",x,"Y: ",y)

#cv2.namedWindow('mouseRGB')

for fgfilename in tqdm(os.listdir(fgdir)):
	outfilename = os.path.join(outdir, fgfilename)
	#if os.path.exists(outfilename):
	#	continue
	fg   = cv2.imread(os.path.join(fgdir, fgfilename),1)
	frameHeight  = np.shape(fg)[0]
	frameWidth   = np.shape(fg)[1]
	
	# Convert BGR to HSV
	hsv = cv2.cvtColor(fg, cv2.COLOR_BGR2HSV)
	
	# define range of green color in HSV
	lower_green = np.array([25,50,30])
	upper_green = np.array([55,255,255])

	# Threshold the HSV image to get only blue colors
	mask = (cv2.inRange(hsv, lower_green, upper_green)/255.0)*90

	#hsvsmall = cv2.resize(hsv[:,:,0], (300,300))
	#cv2.imshow('mouseRGB',hsvsmall)
	#masksmall = cv2.resize(mask, (300,300))
	#cv2.imshow('image',masksmall)
	#cv2.setMouseCallback('image',mouseRGB, masksmall)
	#cv2.waitKey(0)
	
	#print(str(hsv[0,0,:]) + " " + str(mask[0,0]))
	hsv[:,:,0] = hsv[:,:,0] + mask
	#print(str(hsv[0,0,:]) + " " + str(mask[0,0]))
	
	#edges = np.repeat(edges[:,:,np.newaxis], 2, axis = 2)
	cv2.imwrite(outfilename,cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR))
	
	