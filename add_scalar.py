import sys
import os
import cv2
import numpy as np
from tqdm import tqdm

fgdir = sys.argv[1]
bgfilename = sys.argv[2]

bg   = cv2.imread(bgfilename,1)

os.mkdir("sum")

for fgfilename in tqdm(os.listdir(fgdir)):
	print(fgfilename)
	#print(bgfilename)
	outfilename = os.path.join("sum", fgfilename)
	#if os.path.exists(outfilename):
	#	continue
	fg   = cv2.imread(os.path.join(fgdir, fgfilename),1)
	print(np.shape(bg))
	maxImg = np.add(fg, bg)
	cv2.imwrite(outfilename,maxImg)
	