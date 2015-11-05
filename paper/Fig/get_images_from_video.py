import os,sys
import cv2

vidpath = "/media/TOURO Mobile/Composed activity 6/Subject_6/84115 6112013/Color/Color.avi"
outpath = "images_video_portada"

os.system('mkdir -p %s'%outpath)

vid = cv2.VideoCapture(vidpath)

for i in range(0,int(vid.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)),8):
    vid.set(cv2.cv.CV_CAP_PROP_POS_FRAMES,i)
    ret,I = vid.read()
    if ret:
        cv2.imwrite(os.path.join(outpath,'image_%05d.png'%i),I)
