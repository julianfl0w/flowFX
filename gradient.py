import sys
import os
import cv2
import numpy as np
from tqdm import tqdm

fgdir = sys.argv[1]
outdir = os.path.dirname(fgdir) + "_grad"

os.mkdir(outdir)

for fgfilename in tqdm(os.listdir(fgdir)):
	outfilename = os.path.join(outdir, fgfilename)
	#if os.path.exists(outfilename):
	#	continue
	fg   = cv2.imread(os.path.join(fgdir, fgfilename),0)
	frameHeight  = np.shape(fg)[0]
	frameWidth   = np.shape(fg)[1]
	
	outimg = cv2.Laplacian(fg,cv2.CV_16S, ksize = 9)
	#edges = np.repeat(edges[:,:,np.newaxis], 2, axis = 2)
	cv2.imwrite(outfilename,outimg)
	