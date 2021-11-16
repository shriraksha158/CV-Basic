import cv2
img=cv2.imread("sample1.jpg")
cv2.imshow("Python Logo", img)
cv2.imwrite("pythonLogo.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
