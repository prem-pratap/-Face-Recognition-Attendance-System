import cv2
img=cv2.imread("./latest4.png", cv2.IMREAD_UNCHANGED)
width=170
height=80
dim=(width,height)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
cv2.imwrite("latest4.png",resized)
