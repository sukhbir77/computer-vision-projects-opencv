import cv2
import numpy as np

def draw_circle(event, x, y, flags, param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), radius = 100, color = (255,0,0), thickness = -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
         cv2.circle(img, (x,y), radius = 100, color = (0,255,0), thickness = -1)

cv2.namedWindow(winname = 'Drawing')
cv2.setMouseCallback('Drawing', draw_circle)

img = np.zeros((512,512,3))

while True:
    
    cv2.imshow('Drawing', img)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()







