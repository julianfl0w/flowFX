ffmpeg -r 30 -i image-%05d.jpg -vcodec libx264 -pix_fmt yuv420p test.mp4
ffmpeg -start_number 450  -r 30 -i image-%05d.jpg -vcodec libx264 -pix_fmt yuv420p test.mp4
ffmpeg -i .\bennedictory.mp4 bennedictory/out%04d.jpg