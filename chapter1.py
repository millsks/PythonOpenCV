import numpy as np
print("Package Imported - numpy")
import cv2
print("Package Imported - cv2")
# Windows and Mac
from PIL import ImageGrab
print("Package Imported - ImageGrab (PIL)")
# # Linux
# import pyscreenshot as ImageGrab
# print("Package Imported - ImageGrab (pyscreenshot)")

# # Read and display an image
# img = cv2.imread("Resources/istockphoto-1279460648-170667a.jpg")
# cv2.imshow("Output", img)
# cv2.waitKey(0)

# # Read and display a video file
# cap = cv2.VideoCapture("Resources/Sample_Video.mp4")
# while cap.isOpened():
#     sucess, img = cap.read()
#     if sucess:
#         cv2.imshow("Video", img)
#     else:
#         break
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Capture video feed from webcam
# cap = cv2.VideoCapture(3)
# cap.set(3,640)
# cap.set(4,480)
# while True:
#     sucess, img = cap.read()
#     if sucess:
#         cv2.imshow("Video", img)
#     else:
#         break
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Grab screen capture
# while True:
#     img = ImageGrab.grab()
#     img_np = np.array(img)
#     cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
#     cv2.imshow("Screen", img_np)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cv2.destroyAllWindows()


# Read and display an image and convert it to gray scale
img = cv2.imread("Resources/istockphoto-1279460648-170667a.jpg")
kernel = np.ones((5,5), np.uint8)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (15,15), 0)
imgCanny = cv2.Canny(img, 50, 50)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)

cv2.imshow("Output - Color", img)
cv2.imshow("Output - Gray", imgGray)
cv2.imshow("Output - Blur", imgBlur)
cv2.imshow("Output - Canny", imgCanny)
cv2.imshow("Output - Dilation", imgDialation)
cv2.waitKey(0)