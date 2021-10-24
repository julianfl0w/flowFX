#syntax: fgdir bgdir
import colour
import os
import cv2
import numpy as np
import sys
fgdir = sys.argv[1]
bgdir = sys.argv[2]

for fgfilename in os.listdir(fgdir):
	fg   = cv2.imread(os.path.join(fgdir, fgfilename),1)
	#print(fg.dtype)
	fg_float = fg.astype(float)
	fg_lab   = cv2.cvtColor(fg, cv2.COLOR_RGB2Lab)
	fg_gray  = cv2.cvtColor(fg, cv2.COLOR_BGR2GRAY)
	diff = np.zeros_like(fg_gray) + 1000
	for bgfilename in os.listdir(bgdir):
		bg = cv2.imread(os.path.join(bgdir, bgfilename),1)
		#bg_float = bg.astype(float)
		#bg_lab   = cv2.cvtColor(bg, cv2.COLOR_RGB2Lab)
		#delta_E = colour.difference.delta_e.delta_E_CIE1976(fg_lab, bg_lab)
		
		bg_gray  = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)
		sub    = np.subtract(fg_gray.astype(float), bg_gray.astype(float))
		abssub = abs(sub)		
		diff   = np.minimum(abssub, diff)
		
	#cv2.imshow('delta_e', cv2.resize(delta_E.astype(np.uint8), (300,900), interpolation = cv2.INTER_AREA))
	cv2.imshow('luma', cv2.resize(diff.astype(np.uint8), (300,900), interpolation = cv2.INTER_AREA))
	cv2.waitKey(1)
	cv2.imwrite(os.path.join("diff", fgfilename),diff.astype(np.uint8))

		