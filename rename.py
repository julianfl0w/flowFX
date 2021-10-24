from tqdm import tqdm
import os
for fgfilename in tqdm(os.listdir('.')):
	if len(fgfilename) == 13:
		outfilename = fgfilename[:6] + "0" + fgfilename[6:]
		print(outfilename)
		os.rename(fgfilename, outfilename)