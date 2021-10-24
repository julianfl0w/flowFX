import sys
import os
import cv2
import numpy as np
from tqdm import tqdm

fgdir = sys.argv[1]
bgdir = sys.argv[2]
outdir = fgdir.replace("\\","").replace(".","") + "_times_" + bgdir.replace("\\","").replace(".","")

os.mkdir(outdir)

for fgfilename, bgfilename in tqdm(zip(os.listdir(fgdir), os.listdir(bgdir))):
	#print(fgfilename)
	#print(bgfilename)
	outfilename = os.path.join(outdir, fgfilename)
	#if os.path.exists(outfilename):
	#	continue
	fg   = cv2.imread(os.path.join(fgdir, fgfilename),1)
	bg   = cv2.imread(os.path.join(bgdir, bgfilename),1)
	
	maxImg = np.multiply(fg, bg/255.0)
	cv2.imwrite(outfilename,maxImg)
	