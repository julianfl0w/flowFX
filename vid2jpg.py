#syntax: invideo, outfolder

import cv2
import sys
import os
vidcap = cv2.VideoCapture(sys.argv[1])
success,image = vidcap.read()
count = 0

#outdirname = sys.argv[1].split('\\')[1].split('.')[0]
outdirname = sys.argv[1].split('.')[0]
os.mkdir(outdirname)

while success:# and count < 10:
  if count < 3330:
    if (count % 100):
       print(count)
    continue
  index = str(count).zfill(5)
  outname = os.path.join(outdirname, "frame" + index + ".jpg")
  print(outname)
  cv2.imwrite(outname, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  #print('Read a new frame: ', success)
  count += 1