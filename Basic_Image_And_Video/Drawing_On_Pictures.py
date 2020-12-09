import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Coordinates for Rectangle
x = width//2
y = height//2

# Width and height
w = width//4
h = height//4

while True:
    ret, frame = cap.read()
    cv2.rectangle(frame, (x, y), (x+w, y+h), color=(0,0,255),thickness= -1)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()