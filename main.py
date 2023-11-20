import cv2
import numpy as np
img = np.zeros((300, 300), dtype=np.uint8)
img[100:200, 100:200] = 255
laplacian = cv2.Laplacian(img, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))
cv2.imshow('Оригинал', img)
cv2.imshow('Оператор Лапласа', laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()

