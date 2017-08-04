import os
import cv2

folders=['drowsy','distracted','attentive']
inputpath='./rawdata'
outputpath='./clippeddata'

for folder in folders:
	videopath=os.path.join(inputpath, folder)
	tripvideos= os.listdir(videopath)
	for tripvideo in tripvideos:
		video= os.path.join(videopath, tripvideo)
		print(video)	
	
