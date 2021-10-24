import sys
import os
import pixellib
import cv2
import numpy as np
from pixellib.semantic import semantic_segmentation
from tqdm import tqdm

segment_image = semantic_segmentation()
segment_image.load_pascalvoc_model("../deeplabv3_xception_tf_dim_ordering_tf_kernels.h5") 

fgdir  = sys.argv[1]
outdir = fgdir + "_mofo"
os.mkdir(outdir)

for fgfilename in tqdm(os.listdir(fgdir)):
	if os.path.exists(os.path.join(outdir, fgfilename)):
		continue
	fg   = cv2.imread(os.path.join(fgdir, fgfilename),1)
	frameHeight  = np.shape(fg)[0]
	frameWidth   = np.shape(fg)[1]
	nxalpha, segoverlay = segment_image.segmentFrameAsPascalvoc(fg)
	alpha = (nxalpha == 15).astype(np.float)
	# the result of segmentation is too small
	beta = cv2.resize(alpha, (int(frameWidth ), int(frameHeight)), interpolation = cv2.INTER_AREA)	
	# apply gaussian blur
	gSize = int(int((int(frameWidth / 15))/2)+1) #yields 35 when width = 1080
	beta = cv2.GaussianBlur(beta, (gSize, gSize), 0)
	# repeat for RGB
	nxceta = np.repeat(beta[:,:,np.newaxis], 3, axis = 2)
	#print(np.subtract(timeArray, timeArray[0]))
	cv2.imwrite(os.path.join(outdir, fgfilename),(nxceta*255).astype(np.uint8))
	