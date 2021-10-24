import sys
import os
import cv2
import numpy as np
from tqdm import tqdm

fgdir = sys.argv[1]
outdir = fgdir + "_dia"

os.mkdir(outdir)

for fgfilename in tqdm(os.listdir(fgdir)):

	outfilename = os.path.join(outdir, fgfilename)
	#if os.path.exists(outfilename):
	#	continue
	fg   = cv2.imread(os.path.join(fgdir, fgfilename),0)
	frameHeight  = np.shape(fg)[0]
	frameWidth   = np.shape(fg)[1]
	
	#kernel = np.ones((3,3),np.uint8)
	#kernel = cv2.getGaussianKernel(191, 0)
	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
	outimg = cv2.dilate(fg,kernel,iterations = 51)
	#edges = np.repeat(edges[:,:,np.newaxis], 2, axis = 2)
	cv2.imwrite(outfilename,outimg)
	