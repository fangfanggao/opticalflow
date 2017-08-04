# Author: Deepak Pathak (c) 2016

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from pdb import set_trace as st
# from __future__ import unicode_literals
import numpy as np
from PIL import Image
import time
import argparse
import pyflow
import cv2
import os


inputpath='../clipped'
outputpath='../flowdata'
folders= ['drowsy', 'distracted', 'attentive']


	
def extractflow(imagepath, outputlocation):

	
	if not os.path.exists(outputlocation):
        	os.makedirs(outputlocation)

	imagelist=os.listdir(imagepath)
	for i in range(len(imagelist) -1):
		image1= imagelist[i]
		image2=imagelist[i+1]
		out_u_image= 'u'+ str(i+1)+ '.jpg'
		out_v_image='v'+ str(i+1) + '.jpg'
		image1path= os.path.join(imagepath, image1)
		image2path= os.path.join(imagepath, image2)
		im1 = np.array(Image.open(image1path))
		im2 = np.array(Image.open(image2path))
		im1 = im1.astype(float) / 255.
		im2 = im2.astype(float) / 255.

		# Flow Options:
		alpha = 0.012
		ratio = 0.75
		minWidth = 20
		nOuterFPIterations = 7
		nInnerFPIterations = 1
		nSORIterations = 30
		colType = 0  # 0 or default:RGB, 1:GRAY (but pass gray image with shape (h,w,1))

		s = time.time()
		u, v, im2W = pyflow.coarse2fine_flow(
		    im1, im2, alpha, ratio, minWidth, nOuterFPIterations, nInnerFPIterations,
		    nSORIterations, colType)

		u = cv2.normalize(u, None, 0, 255, cv2.NORM_MINMAX)
		v = cv2.normalize(v, None, 0, 255, cv2.NORM_MINMAX)
		cv2.imwrite(os.path.join(outputlocation, out_u_image), u)
		cv2.imwrite(os.path.join(outputlocation, out_v_image), v)

inputpath='../clipped'
outputpath='../flowdata'
folders= ['drowsy', 'distracted', 'attentive']

for folder in folders:
	inpath= os.path.join(inputpath, folder)
	trips=os.listdir(inpath)
	for tripfolder in trips:
		tripimagepath=os.path.join(inpath, tripfolder)
		outflowpath= os.path.join(outputpath, folder, tripfolder);
		extractflow(tripimagepath,outflowpath)
		
	
