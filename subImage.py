import numpy as np
import cv2
#config
PicName="sample.png"
SubSize = 0.2 #
strides = 10





im = cv2.imread(PicName)
#print len(im),len(im[0])#height,width
SourceH = len(im)
SourceW = len(im[0])
SubH = int(SourceH*SubSize)
SubW = int(SourceW*SubSize)
print SubH,SubW
StartPointH = 0
StartPointW = 0
switch = True
index = 1
while switch:
            
    EndPointH = int(StartPointH+SubH)
    EndPointW = int(StartPointW+SubW)
    print StartPointH,EndPointH
    if not EndPointH > SourceH:
        cv2.imwrite('./output/sub_'+str(index)+'.png',im[StartPointH:EndPointH,StartPointW:EndPointW])
        StartPointH+=strides
    else:
        StartPointH=0
        StartPointW+=strides
        if StartPointW+SubW > SourceW:
            switch = False
    index = int(index)+1
    
