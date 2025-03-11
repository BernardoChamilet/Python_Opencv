import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Lendo imagem
img = cv.imread("Cinza.jpg", 0)
# Equalizando imagem 
imgEqualizada = cv.equalizeHist(img)
# Gerando histograma de intensidade de pixels da imagem com matriz de uma dimensão feita a partir da imagem com img.ravel
plt.hist(imgEqualizada.ravel(), 256, [0,256])
plt.title("Histograma de Intensidade")
plt.xlabel("Intensidade de Pixel")
plt.ylabel("Frequência")
plt.show()

# Lendo imagem no formato bgr (matriz com intensidade de cada cor em cada pixel)
img = cv.imread("colorida.jpg")

# Dividindo matriz em 3, uma para cada cor
azul, verde, vermelho = cv.split(img)

# Criando figura para exibir os três histogramas
fig = plt.figure(figsize=(20,5))

ax1 = fig.add_subplot(131) # 1 linha 3 colunas 1 posição
ax1.hist(azul.ravel(), 256, [0,256])
plt.title("Histograma do canal azul")

ax2 = fig.add_subplot(132)
ax2.hist(verde.ravel(), 256, [0,256])
plt.title("Histograma do canal verde")

ax3 = fig.add_subplot(133)
ax3.hist(vermelho.ravel(), 256, [0,256])
plt.title("Histograma do canal vermelho")

plt.show()