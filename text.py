# -*- coding: utf-8 -*-

"""

Created on Wed Aug 29 21:48:21 2018

 
@author: Miracle

 
"""

import cv2

 
def detectFace():

#加载人脸检测的配置文件

    face_cascade1 = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    face_cascade2 = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    face_cascade3 = cv2.CascadeClassifier('haarcascade_frontalface_alt_tree.xml')
    face_cascade4 = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    #判断是否可行

    if face_cascade1.empty() or face_cascade2.empty() or face_cascade3.empty() or face_cascade4.empty():

        raise IOError('Cannot load cascade classifier xml files!')
    print(1)
    #打开摄像头 
    cap = cv2.VideoCapture('f.png')
    
    print(1)
    scaling_factor = 1.15
    if not cap.isOpened:

        raise IOError('Cannot open webcam!')

 
    while True:

        ret,frame = cap.read()

        if not ret:

            break

        frame = cv2.resize(frame,None,

        fx = scaling_factor,

        fy = scaling_factor,

        interpolation = cv2.INTER_LINEAR)

        
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        ss = [face_cascade1,face_cascade2,face_cascade3,face_cascade4]
        #获取脸部位置
        for i in ss:
            face_rects = i.detectMultiScale(gray)

            
            #获取脸部地址

            for (x,y,w,h) in face_rects:

                roi_gray = gray[y:y+h,x:x+h]

                roi_color = frame[y:y+h,x:x+h]

                center = (x,y)

                radius = 20

                color = (0,255,0)

                thickness = 3
                print(x,y)
                img = cv2.circle(roi_color,center,radius,color,thickness)

            
                cv2.imshow('detecting eye',img)
                cv2.waitKey(0)
                
                if cv2.waitKey(1) == 27:

                    break

    cap.release()

    cv2.destroyAllWindows()

 
if __name__ == '__main__':

    detectFace()