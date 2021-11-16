import cv2
img = cv2.imread("sample1.jpg")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("grayImage.jpg", grayImg)
cv2.imshow("Original", img)
cv2.imshow("Gray Image", grayImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
