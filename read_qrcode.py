# read qrcode

import cv2


qrcode_detector = cv2.QRCodeDetector()

values, points, qrcode_data = qrcode_detector.detectAndDecode(
    cv2.imread("img/qrcode.png")
)

print(values)
