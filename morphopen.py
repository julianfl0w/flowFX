import sys
import os
import cv2
import numpy as np
from tqdm import tqdm

fgdir = sys.argv[1]
outdir = fgdir + "_open"

os.mkdir(outdir)
count = 0
for fgfilename in tqdm(os.listdir(fgdir)):
	outfilename = os.path.join(outdir, fgfilename)
	#if os.path.exists(outfilename):
	#	continue
	fg   = cv2.imread(os.path.join(fgdir, fgfilename),0)
	frameHeight  = np.shape(fg)[0]
	frameWidth   = np.shape(fg)[1]
	
	#kernel = np.ones((3,3),np.uint8)
	#kernel = cv2.getGaussianKernel(191, 0)
	#kernel  = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
	#cv.MORPH_OPEN, 1: cv.MORPH_CLOSE, 2: cv.MORPH_GRADIENT, 3: cv.MORPH_TOPHAT, 4: cv.MORPH_BLACKHAT}
	morph_size  = 30
	element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*morph_size + 1, 2*morph_size+1), (morph_size, morph_size))
	for i in range(5):
		fg  = cv2.morphologyEx(fg, cv2.MORPH_OPEN, element)
	#edges = np.repeat(edges[:,:,np.newaxis], 2, axis = 2)
	cv2.imwrite(outfilename,fg)
	count += 1
	#if count > 10:
	#	break