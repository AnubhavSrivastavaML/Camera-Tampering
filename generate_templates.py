import cv2

def get_templates(image,points , n):
    template_images=[]
    for (x,y) in points:
        template_images.append(image[y:y+n,x:x+n])
    return template_images

