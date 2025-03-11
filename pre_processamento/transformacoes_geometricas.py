import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Lendo imagem
img = cv.imread("Cinza.jpg", 0)

# Obtendo total de linhas e colunas da matriz
totalLinhas, totalColunas = img.shape

# Obtendo matriz de rotação. Parâmetros: centro da matriz, ângulo que deseja rotacionar, escala
matriz_de_rotacao = cv.getRotationMatrix2D((totalLinhas/2, totalColunas/2), 45, 1)

# Obtendo imagem rotacionada
imgRotacionada = cv.warpAffine(img, matriz_de_rotacao, (totalColunas, totalLinhas))

# Mudando tamanho da imagem
imgDiminuida = cv.resize(img,
                         None,
                         fx = 0.8,
                         fy = 0.8,
                         interpolation = cv.INTER_CUBIC)

# Deslocando imagem 
matriz  = np.float32([[1,0,100],[0,1,100]])
imgDeslocada = cv.warpAffine(img, matriz, (totalColunas, totalLinhas))

# Para somar, subtrair ou mesclar imagens use funções add, subtract e addWeighted do opencv

# Exibindo a imagem rotacionada
plt.imshow(imgRotacionada, cmap="gray")
plt.title("Imagem Rotacionada")
plt.axis("off") 
plt.show()