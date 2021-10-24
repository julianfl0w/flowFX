#syntax: invideo, outfolder

import cv2
import sys
import os
import re

infilename = sys.argv[1]
vidcap = cv2.VideoCapture(infilename)
success,image = vidcap.read()
count = 0
outdir = "".join(re.findall("[a-zA-Z]+", infilename))

print("outdir " + outdir)
os.mkdir(outdir)

while count < int(sys.argv[2]):# and count < 10:
	index = str(count).zfill(5)
	outfilename = os.path.join(outdir, "frame" + index + ".jpg")
	success,image = vidcap.read()
	if success:
		cv2.imwrite(outfilename, image)     # save frame as JPEG file      
	else:
		print('resetting video')
		vidcap.set(cv2.CAP_PROP_POS_FRAMES, 0)
		continue
	print('Read a new frame: ', success)
	count += 1