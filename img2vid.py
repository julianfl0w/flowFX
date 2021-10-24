
import cv2
import os
import sys
from tqdm import tqdm
import skvideo

pathStr  = str('C:/Users/jcloi/Downloads/ffmpeg-N-101017-gcfcc36240f-win64-gpl-shared/ffmpeg-N-101017-gcfcc36240f-win64-gpl-shared/bin')
skvideo.setFFmpegPath(pathStr)
import skvideo.io
import skvideo.datasets
import skvideo.utils
print(skvideo.__file__)

image_folder = sys.argv[1]
video_name = image_folder.replace("\\","").replace(".","") + ".mp4"

images = [img for img in os.listdir(image_folder)]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

#fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#video = cv2.VideoWriter(video_name, fourcc, 30, (width,height))
#
#for image in tqdm(images):
#    video.write(cv2.imread(os.path.join(image_folder, image)))
#
#cv2.destroyAllWindows()
#video.release()

#skvideo.io.vwrite(outvideofile, outvideo, inputdict={
#  '-r': fps,
#})
		
writer = skvideo.io.FFmpegWriter(video_name, inputdict={
  '-r': "30",
}, outputdict={
    '-vcodec': 'libx264'
})
for image in tqdm(images):
	img = cv2.imread(os.path.join(image_folder, image))
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	#cv2.imshow('luma', cv2.resize(img, (300,900), interpolation = cv2.INTER_AREA))
	#cv2.waitKey(0)
	writer.writeFrame(img)
writer.close()