import sys
import os
import cv2
import numpy as np
from tqdm import tqdm
from scipy.signal import convolve2d

# http://jakevdp.github.io/blog/2013/08/07/conways-game-of-life/
def life_step_1(X):
    """Game of life step using generator expressions"""
    nbrs_count = sum(np.roll(np.roll(X, i, 0), j, 1)
                     for i in (-1, 0, 1) for j in (-1, 0, 1)
                     if (i != 0 or j != 0))
    return (nbrs_count == 3) | (X & (nbrs_count == 2))

def life_step_2(X):
    """Game of life step using scipy tools"""
    nbrs_count = convolve2d(X, np.ones((3, 3)), mode='same', boundary='wrap') - X
    return (nbrs_count == 3) | (X & (nbrs_count == 2))
	
def life_step_J(X):
    """Game of life step using scipy tools"""
    nbrs_count = convolve2d(X, np.ones((3, 3)), mode='same', boundary='fill')
    return (nbrs_count > 5)
	
fgdir = sys.argv[1]
outdir = os.path.dirname(fgdir) + "_conway"

os.mkdir(outdir)

for fgfilename in tqdm(os.listdir(fgdir)):
	outfilename = os.path.join(outdir, fgfilename)
	#if os.path.exists(outfilename):
	#	continue
	fg   = cv2.imread(os.path.join(fgdir, fgfilename),0)
	frameHeight  = np.shape(fg)[0]
	frameWidth   = np.shape(fg)[1]
	
	kernel = cv2.getGaussianKernel(11, 1.5)
	outimg = cv2.filter2D(fg, -1, kernel)[5:-5, 5:-5] # valid
	outimg = (outimg > 4)*255
	
	#print(np.shape(outimg))
	#edges = np.repeat(edges[:,:,np.newaxis], 2, axis = 2)
	cv2.imwrite(outfilename,outimg)
	