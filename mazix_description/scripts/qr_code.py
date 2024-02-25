import cv2

img=cv2.imread('/home/ferbin/mazix_ws/src/mazix_description/qr/Left.png')

decoder = cv2.QRCodeDetector()
data, points,_ = decoder.detectAndDecode(img)

print("Results:",data)

cv2.imshow('Detected QR code',img)
cv2.waitKey()
cv2.destroyAllWindows()