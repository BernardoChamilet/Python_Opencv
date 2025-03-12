import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('einstein.png')

imgM = cv.blur(img, (5,5))

fig = plt.figure(figsize=(20,50))
ax1 = fig.add_subplot(121)
plt.imshow(img)
plt.title("Imagem com ruído")

ax2 = fig.add_subplot(122)
plt.imshow(imgM)
plt.title("Imagem Filtrada")
plt.show()