import sys
import os
import cv2
import numpy as np
from tqdm import tqdm

fgdir = sys.argv[1]
outdir = sys.argv[2]


for fgfilename in tqdm(os.listdir(fgdir)):
	outfilename = os.path.join(outdir, fgfilename)
	#if os.path.exists(outfilename):
	#	continue
	fg   = cv2.imread(os.path.join(fgdir, fgfilename),0)
	frameHeight  = np.shape(fg)[0]
	frameWidth   = np.shape(fg)[1]
	
	ret,thresh1 = cv2.threshold(fg,180,255,cv2.THRESH_BINARY)
	gSize = int(int((int(frameWidth / 15))/2)+1) #yields 35 when width = 1080
	thresh1 = cv2.GaussianBlur(thresh1, (gSize, gSize), 0)
	cv2.imwrite(outfilename,thresh1)
	