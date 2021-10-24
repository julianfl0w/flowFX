import cv2
import sys
import os
import numpy as np
import skvideo
pathStr  = str('C:/Users/jcloi/Downloads/ffmpeg-N-101017-gcfcc36240f-win64-gpl-shared/ffmpeg-N-101017-gcfcc36240f-win64-gpl-shared/bin')
skvideo.setFFmpegPath(pathStr)
import skvideo.io
import skvideo.datasets
import skvideo.utils
import time
from tqdm import tqdm
#from itertools import cycle


# apply fg overlay to a list of videos over a bg
def replaceFgAndBg(fg, bg, alpha):
 
	#print("replacing fg")
	#Return an array of zeros with the same shape and type as a given array
	#outvideo = np.zeros_like(bg)
	
	#cv2.imshow('luma', cv2.resize(fg.astype(np.uint8), (300,900), interpolation = cv2.INTER_AREA))
	#cv2.waitKey(1)
	# create a positive mask based on the img
	alpha = alpha.astype(np.float)/255.0
	#print(np.shape(alpha))
	#print(np.shape(fg))
	foreground = cv2.multiply(alpha, fg, dtype=cv2.CV_8U) #remove from extant fg
	
	
	#remove this mask from bg
	background = cv2.multiply(1-alpha, bg, dtype=cv2.CV_8U) 
	retval = np.add(foreground, background)
	return retval
	
if __name__ == "__main__":
	if len(sys.argv) != 4:
		print("syntax: python replaceFgAndBg.py bgdir fg0 mx0")
		sys.exit()
	bgdir  = sys.argv[1]
	
	fgdir  = sys.argv[2]
	mxdir  = sys.argv[3]
	
	outdir = os.path.dirname(fgdir).replace("\\","").replace(".","") + "_with_" + \
	os.path.dirname(bgdir).replace("\\","").replace(".","") + "_with_" + \
	os.path.dirname(mxdir).replace("\\","").replace(".","")
	
	os.mkdir(outdir)
	#bgcyc = pool = cycle(lst)

	for bgfilename, fgfilename, mxfilename in tqdm(zip(os.listdir(bgdir), os.listdir(fgdir), os.listdir(mxdir))):
	
		outfilename = os.path.join(outdir, fgfilename)
		if os.path.exists(outfilename):
			continue
				
		mx   = cv2.imread(os.path.join(mxdir, mxfilename),1)
		frameHeight  = np.shape(mx)[0]
		frameWidth   = np.shape(mx)[1]
		bg   = cv2.imread(os.path.join(bgdir, bgfilename),1)
		bg   = cv2.resize(bg, (int(frameWidth ), int(frameHeight)), interpolation = cv2.INTER_AREA)
		fg   = cv2.imread(os.path.join(fgdir, fgfilename),1)
		fg   = cv2.resize(fg, (int(frameWidth ), int(frameHeight)), interpolation = cv2.INTER_AREA)	
		result = replaceFgAndBg(fg, bg, mx)
		cv2.imwrite(outfilename,result)