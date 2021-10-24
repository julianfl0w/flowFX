import sys
import os
import cv2
import numpy as np
from tqdm import tqdm

fgdir = sys.argv[1]
outdir = sys.argv[2]

init = False 
for fgfilename in tqdm(os.listdir(fgdir)):
	outfilename = os.path.join(outdir, fgfilename)
	#if os.path.exists(outfilename):
	#	continue
	fg   = cv2.imread(os.path.join(fgdir, fgfilename),0)
	if not init:
		fg_last = np.zeros_like(fg)
		init = True
	#print(fg_last.shape)
	retval, residual_thresh = cv2.threshold(fg_last*0.85,20,255,cv2.THRESH_TOZERO)
	#print(np.shape(residual_thresh))
	outimg = np.add(fg, residual_thresh)
	cv2.imwrite(outfilename,outimg)
	fg_last = outimg