import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('formas.png')

imgGauss = cv.GaussianBlur(img, (5,5), 0)

fig = plt.figure(figsize=(20,50))
ax1 = fig.add_subplot(121)
plt.imshow(img)

ax2 = fig.add_subplot(122)
plt.imshow(imgGauss)
plt.show()