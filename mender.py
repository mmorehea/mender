import os
import sys
import tifffile
import code
import numpy as np
#import cv2
import glob

def consecutive(data, stepsize=1):
    return np.split(data, np.where(np.diff(data) != stepsize)[0]+1)





def messRow(mask, img):
    for row in range(mask.shape[0]):
        whites = np.where(mask[row, :] == 1)
        count = whites[0].size
        if count == 0:
            continue
        oldRow = img[row, :]
        code.interact(local=locals())
        newRow = np.delete(oldRow, whites[0])
        while len(newRow) < len(oldRow):
            newRow = np.append(newRow, 0)
        #code.interact(local=locals())
        img[row, :] = newRow
    return img


def findWhiteWidth(mask):
    arr = []
    for row in range(mask.shape[0]):
        white = np.where(mask[row, :] == 1)
        whiteWidth = white[0].size
        arr.append(whiteWidth)
    return arr

#def threes(arr):
#   for val in range(arr)
#      mod = arr[val,:]
#        num = mod % 3
#       if num == 0:
#            newnum = mod
#        if num == 1:
#            newnum = mod + 1
#        if num == 2:
#            newnum = mod - 1
#        arr.append(newnum)
#    return arr

def findMin(arr):
    minVal = min(arr)
    return arr


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
    minVal = findMin(widths)
 #   roundWidths = threes(widths)
    code.interact(local=locals())
