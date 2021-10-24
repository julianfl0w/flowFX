import sys
import os
import cv2
import numpy as np
from tqdm import tqdm

fgdir = sys.argv[1]
bgdir = sys.argv[2]

outdir = os.path.dirname(fgdir) + "_sub"

os.mkdir(outdir)

for fgfilename in tqdm(os.listdir(fgdir)):
	#print(fgfilename)
	#print(bgfilename)
	outfilename = os.path.join(outdir, fgfilename)
	#if os.path.exists(outfilename):
	#	continue
	fg   = cv2.imread(os.path.join(fgdir, fgfilename),1)
	
	minImg = np.add(np.zeros_like(fg), 255)
	for bgfilename in tqdm(os.listdir(bgdir)):
		bg       = cv2.imread(os.path.join(bgdir, bgfilename),1)
		#print(np.shape(bg))
		#print(np.shape(fg))
		diff     = np.subtract(fg.astype(np.int32), bg.astype(np.int32))
		thisDiff = np.abs(diff).astype(np.uint8)
		minImg   = np.minimum(minImg, thisDiff)
	cv2.imwrite(outfilename,minImg)
	