import cv2

# Initialize Video Capture, create a video capture object

cap= cv2.VideoCapture(0)

if not cap.isOpened():
    print('Could not open the camera')
    exit()
#Capture image when we press 'c' on the keyboard

while(True):
    ret,frame = cap.read() 
    cv2.imshow("Live Video",frame)


    if(cv2.waitKey(1)  & 0xFF == ord('c')):
        cv2.imwrite(r"C:\Users\kouadio\Robox\Dataset\Camera1\condensateur.jpg",frame)





