import sys
import os
import cv2
import numpy as np
from tqdm import tqdm

fgdir = sys.argv[1]
bgdir = sys.argv[2]

for fgfilename, bgfilename in tqdm(zip(os.listdir(fgdir), os.listdir(bgdir))):
	print(fgfilename)
	print(bgfilename)
	outfilename = os.path.join("sum", fgfilename)
	#if os.path.exists(outfilename):
	#	continue
	fg   = cv2.imread(os.path.join(fgdir, fgfilename),0)
	bg   = cv2.imread(os.path.join(bgdir, bgfilename),0)
	
	maxImg = np.max(fg, bg)
	cv2.imwrite(outfilename,maxImg)
	