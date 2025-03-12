import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('head.png')

imgMed = cv.medianBlur(img, 5)

fig = plt.figure(figsize=(20,50))

ax1 = fig.add_subplot(121)
plt.imshow(img)

ax2 = fig.add_subplot(122)
plt.imshow(imgMed)
plt.show()