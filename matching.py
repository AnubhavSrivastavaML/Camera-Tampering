import cv2

def match(temp,frame_templates):
    count = 0
    for (img0,img1) in zip(temp,frame_templates):
        res = cv2.matchTemplate(img0,img1,cv2.TM_CCOEFF_NORMED) 
        if res[0][0]>0.8 :
            count+=1
    return count

