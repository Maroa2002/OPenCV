import cv2 as cv

# _____________ Open a capturing device video capturing __________#
cam = cv.VideoCapture(2)

# _____________ Detect objects in other images using CascadeClassifier() function __________#
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_alt.xml")
eye_cascade = cv.CascadeClassifier(" haarcascade_eye_tree_eyeglasses.xml")
while True:
    # _______ Reading Video using the read() function ______ #
    # ret is a boolean that checks whether the camera is on or not and the frame is a variable that stores the data read
    ret, frame = cam.read()

    # Color space conversion from Coloured BGR to grayscale
    gray_scale_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # if camera is not opened then just continue
    if not ret:
        continue

    # function is used to detect the faces. This function will return a rectangle with coordinates(x,y)
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)

    if len(faces) == 0:
        continue

    # display the video with a title "Video Frame"
    # The code below has the same meaning with the code, if ret == False since it is a boolean
    cv.imshow("Video Frame", frame)

    # storing the key to be presses in a variable named key
    key = cv.waitKey(1) & 0xFF

    # Checking if the key pressed is the same as the stored key and if true then basically terminate the whole process
    if key == ord("q"):
        break
# Close the webcam once the whole process is done
cam.release()
cv.destroyAllWindows()
