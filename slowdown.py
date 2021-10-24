import sys
import os
import cv2
import numpy as np
from tqdm import tqdm

fgdir = sys.argv[1]
slowdown = int(sys.argv[2])
framecount = int(sys.argv[3])
count  = 0
outdir = os.path.dirname(fgdir) + "_slow"
os.mkdir(outdir)


for fgfilename in tqdm(os.listdir(fgdir)):
	fgIndex = int(fgfilename[-9:-4])
	outfilename = os.path.join(outdir, fgfilename)
	#if os.path.exists(outfilename):
	#	continue
	fg   = cv2.imread(os.path.join(fgdir, fgfilename),1)
	frameHeight  = np.shape(fg)[0]
	frameWidth   = np.shape(fg)[1]
	
	for i in range(slowdown):
		outfilenamelist = list(outfilename)
		outfilenamelist[-9:-4] = str(count).zfill(5)
		outfilename = ''.join(outfilenamelist)
		cv2.imwrite(outfilename,fg)
		count += 1
	
	if count > framecount:
		break
	