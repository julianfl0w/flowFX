import sys
import os
import cv2
import numpy as np
from tqdm import tqdm

fgdir = sys.argv[1]
bgfilename = sys.argv[2]

bg   = cv2.imread(bgfilename,1)

os.mkdir("sub")

for fgfilename in tqdm(os.listdir(fgdir)):
	print(fgfilename)
	#print(bgfilename)
	outfilename = os.path.join("sub", fgfilename)
	#if os.path.exists(outfilename):
	#	continue
	fg   = cv2.imread(os.path.join(fgdir, fgfilename),1)
	print(np.shape(bg))
	maxImg = np.abs(np.subtract(fg.astype(np.integer), bg.astype(np.integer))).astype(np.uint8)
	cv2.imwrite(outfilename,maxImg)
	