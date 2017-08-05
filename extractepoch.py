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
                vidcap = cv2.VideoCapture(video)
                starttime=20000
                endtime=40000
                vidcap.set(cv2.CAP_PROP_POS_MSEC, starttime)
                while True:
                    success,image = vidcap.read()
                    currentime= vidcap.get(cv2.CAP_PROP_POS_MSEC)
                    if(currentime> endtime):
                        break
                    if success:
                        filename='image'+ str(i)+ '.jpg'
                        cv2.imwrite(filename, image)
                    else:
                        break
