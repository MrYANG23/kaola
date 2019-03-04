import cv2
vc=cv2.VideoCapture('/home/yh/下载/output32.mp4')
c=1

if vc.isOpened():
    rval,frame=vc.read()
else:
    rval=False

time_F=50
while rval:
    rval,frame=vc.read()
    if (c%time_F==0):
        print('--------------jiance')
        cv2.imwrite('/home/yh/shujuji/vedio/image/'+str(c)+'.png',frame)
    c=c+1
    print('--------------------c',c)

vc.release()