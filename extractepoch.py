import os
import cv2
from pdb import set_trace as st
folders=['drowsy','distracted','attentive']
inputpath='./rawdata'
outputpath='./clipped'

for folder in folders:
	videopath=os.path.join(inputpath, folder)
	tripvideos= os.listdir(videopath)
	for tripvideo in tripvideos:
		tripimagesfolder=os.path.splitext(tripvideo)
		outpath= os.path.join(outputpath,folder, tripimagesfolder[0])
		if not os.path.exists(outpath):
			os.makedirs(outpath)
		video= os.path.join(videopath, tripvideo)
		vidcap = cv2.VideoCapture(video)
		starttime=20000
		endtime=40000
		vidcap.set(cv2.CAP_PROP_POS_MSEC, starttime)
		i=1
		while True:
			success,image = vidcap.read()
			currentime= vidcap.get(cv2.CAP_PROP_POS_MSEC)
			if(currentime> endtime):
				break
			if success:
				filename='image'+ str(i)+ '.jpg'				
				cv2.imwrite(os.path.join(outpath,filename), image)
				i+=1
			else:
				break
