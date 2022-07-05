# ----------------------------Importing the OpenCV library ------------------------------- #
import cv2

# ----------------------------Reading the image using imread() function ------------------------------- #
image = cv2.imread('graf1.png', -1)

# ----------------------------Displaying the matrix of the image ------------------------------- #
print(image)

# ----------------------------Displaying the image using imshow() function------------------------------- #
cv2.imshow("Sample", image)
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()

# ----------------------------Writing an image using the imwrite() function------------------------------- #
elif key == ord("s"):
    cv2.imwrite("graf1_copy.png", image)
    cv2.destroyAllWindows()

# ----------------------------Extracting the height and width of an image------------------------------- #
h, w = image.shape[:2]

# ----------------------------Displaying the height and width------------------------------- #
print("Height = {},  Width = {}".format(h, w))
