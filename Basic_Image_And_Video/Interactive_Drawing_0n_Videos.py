import cv2
# Create a function based on a CV2 Event (Left button click)

# mouse callback function
'''def draw_rectangle(event,x,y,flags,param):

    global pt1,pt2,topLeft_clicked,botRight_clicked

    # get mouse click
    if event == cv2.EVENT_LBUTTONDOWN:
        
        #Reset the rectangle
        if topLeft_clicked == True and botRight_clicked == True:
            topLeft_clicked = False
            botRight_clicked = False
            pt1 = (0,0)
            pt2 = (0,0)

        if topLeft_clicked == False:
            pt1 = (x,y)
            topLeft_clicked = True
            
        elif botRight_clicked == False:
            pt2 = (x,y)
            botRight_clicked = True

        
# Haven't drawn anything yet!

pt1 = (0,0)
pt2 = (0,0)
topLeft_clicked = False
botRight_clicked = False

cap = cv2.VideoCapture(0) 

# Create a named window for connections
cv2.namedWindow('Test')

# Bind draw_rectangle function to mouse cliks
cv2.setMouseCallback('Test', draw_rectangle) 


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if topLeft_clicked:
        cv2.circle(frame, center=pt1, radius=2, color=(0,0,255), thickness=-1)
        
    #drawing rectangle
    if topLeft_clicked and botRight_clicked:
        cv2.rectangle(frame, pt1, pt2, (0, 0, 255), 2)
        
        
    # Display the resulting frame
    cv2.imshow('Test', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()

'''

# Create a function based on a CV2 Event (Left button click)

# mouse callback function
def draw_circle(event,x,y,flags,param):

    global center,clicked

    # get mouse click on down and track center
    if event == cv2.EVENT_LBUTTONDOWN:
        center = (x, y)
        clicked = False
    
    # Use boolean variable to track if the mouse has been released
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

        
# Haven't drawn anything yet!
center = (0,0)
clicked = False


# Capture Video
cap = cv2.VideoCapture(0) 

# Create a named window for connections
cv2.namedWindow('Test')

# Bind draw_rectangle function to mouse cliks
cv2.setMouseCallback('Test', draw_circle) 


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Use if statement to see if clicked is true
    if clicked==True:
        # Draw circle on frame
        cv2.circle(frame, center=center, radius=50, color=(255,0,0), thickness=5)
        
    # Display the resulting frame
    cv2.imshow('Test', frame)

    # This command let's us quit with the "q" button on a keyboard.
    # Simply pressing X on the window won't work!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()