import sys
import os
import cv2
import numpy as np
from tqdm import tqdm

fgdir = sys.argv[1]
outdir = os.path.dirname(fgdir) + "_inv"

os.mkdir(outdir)

for fgfilename in tqdm(os.listdir(fgdir)):
	outfilename = os.path.join(outdir, fgfilename)
	#if os.path.exists(outfilename):
	#	continue
	fg   = cv2.imread(os.path.join(fgdir, fgfilename),0)
	frameHeight  = np.shape(fg)[0]
	frameWidth   = np.shape(fg)[1]
	
	outimg = 255 - fg
	outimg = cv2.bitwise_not(fg)
	#edges = np.repeat(edges[:,:,np.newaxis], 2, axis = 2)
	cv2.imwrite(outfilename,outimg)
	