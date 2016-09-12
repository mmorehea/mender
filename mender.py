import os
import sys
import tifffile
import code
import numpy as np
import cv2
import glob
import time

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
			firsts.append(-1)
			continue
		first = white[0][0]
		firsts.append(first)
	return firsts


def findMin(arr):
	arr = filter(lambda a: a != 0, arr)
	std = np.std(arr)
	mean = np.mean(arr)
	gap = int(mean + 2*std)
	#code.interact(local=locals())
	return gap

def shift(mask, img, firstWhite, gap):
	for each in firstWhite:
		if each != -1:
			lastWhite = each
			break

	add = np.zeros(gap, dtype=np.int)
	newImg = []
	for row in range(mask.shape[0]):
		oldRow = img[row, :]
		if firstWhite[row] != -1:
			lastWhite = firstWhite[row]
			indexesToDelete = range(firstWhite[row], firstWhite[row]+gap)
			cutRow = np.delete(oldRow, indexesToDelete)
			newRow = np.append(cutRow,add)
			if row == 0:
				newImg = newRow
			if row != 0:
				newImg = np.vstack((newImg, newRow))
		else:
			indexesToDelete = range(lastWhite, lastWhite+gap)
			cutRow = np.delete(oldRow, indexesToDelete)
			newRow = np.append(cutRow,add)
			if row == 0:
				newImg = newRow
			if row != 0:
				newImg = np.vstack((newImg, newRow))



	#code.interact(local=locals())
	return newImg

start = time.time()



imgs = sys.argv[1]
mask = sys.argv[2]
output = sys.argv[3]

imgL = sorted(glob.glob(imgs + '*.tiff'))
maskL = sorted(glob.glob(mask + '*.tiff'))
outputCount = sorted(glob.glob(output + '*.tiff'))
#code.interact(local=locals())
for ii, each in enumerate(imgL):
	if ii < len(outputCount):
		continue
	end = time.time()
	print(end - start)
	print (ii)
	impath = imgL[ii]
	img = tifffile.imread(impath)
	maskpath = maskL[ii]
	mask = tifffile.imread(maskpath)
	widths = findWhiteWidth(mask)
	gap  = findMin(widths)
	firstWhite = findFirst(mask)
	mendImg = shift(mask, img, firstWhite, gap)
	cv2.imwrite(output + each.split('/')[-1], mendImg)

code.interact(local=locals())
