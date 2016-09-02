import os
import sys
import tifffile
import code
import numpy as np
import cv2
import glob

def consecutive(data, stepsize=1):
    return np.split(data, np.where(np.diff(data) != stepsize)[0]+1)





#def messRow(mask, img):
#    for row in range(mask.shape[0]):
#        whites = np.where(mask[row, :] == 1)
#        count = whites[0].size
#        if count == 0:
#            continue
#        oldRow = img[row, :]
#        code.interact(local=locals())
#        newRow = np.delete(oldRow, whites[0])
#        while len(newRow) < len(oldRow):
#            newRow = np.append(newRow, 0)
#        #code.interact(local=locals())
#        img[row, :] = newRow
#    return img


def findWhiteWidth(mask):
    arr = []
    for row in range(mask.shape[0]):
        white = np.where(mask[row, :] == 1)
        whiteWidth = white[0].size
        arr.append(whiteWidth)
    return arr


def findFirst(mask):
	firsts = []
	for row in range(mask.shape[0]):
		white = np.where(mask[row, :] == 1)
		count = white[0].size
		if count == 0:
			continue
		first = white[0][0]
		firsts.append(first)
	return firsts


def findMin(arr):
	arr.sort()
	gap = arr[-1]
	return gap

def preShift(firstWhite, gap):
	array1 = []
	array2 = []
	for x in range(len(firstWhite)):
		first = firstWhite[x]
		z = 0
		for y in range(gap):
			array1.append(first+z)
			z = z+1
	return array1


def shift(mask, img, indicies):

	z = 0
	for row in range(mask.shape[0]):
		oldRow = img[row, :]

		for x in range(30):
			newRow = np.delete(oldRow, indicies[z])
			oldRow = newRow
			z = z + 1
		code.interact(local=locals())
		img[row, :] = newRow
	return img







imgL = sorted(glob.glob('./test_em/*.tiff'))
maskL = sorted(glob.glob('./test_mask/*.tiff'))
#code.interact(local=locals())
for ii, each in enumerate(imgL):
	print (ii)
	impath = imgL[ii]
	img = tifffile.imread(impath)
	maskpath = maskL[ii]
	mask = tifffile.imread(maskpath)
	widths = findWhiteWidth(mask)
	gap  = findMin(widths)
	firstWhite = findFirst(mask)
	indicies = preShift(firstWhite, gap)
	mendImg = shift(mask, img, indicies)
	code.interact(local=locals())
