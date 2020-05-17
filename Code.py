import cv2

#############################################
frameWidth = 640
frameHeight = 480
nPlateCascade = cv2.CascadeClassifier("Files/haarcascade_russian_plate_number.xml")
minArea = 200
color = (255,0,255)
###############################################
cap = cv2.VideoCapture(0)           #Capture video from webcam
cap.set(3, frameWidth)              #Setting the resolution and brightness level of the video
cap.set(4, frameHeight)
cap.set(10,150)
count = 0

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                 # Convert image to grayscale
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)                 # Use the grayscale image to find numberplates in the image using the russian number plate cascade
    for (x, y, w, h) in numberPlates:
        area = w*h                                                                  # Calculate the area of the contours and select the contours with area<400 to eliminate the unnecessary noise
        if area >minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)            # Enclose the selected region within a rectangle and add a text next to it
            cv2.putText(img,"Number Plate",(x,y-5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgRoi = img[y:y+h,x:x+w]                                               # Crop the obtained region of interest and display it separately
            cv2.imshow("ROI", imgRoi)

    cv2.imshow("Result", img)                                                       

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("Resources/Scanned/NoPlate_"+str(count)+".jpg",imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,
                    2,(0,0,255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count +=1