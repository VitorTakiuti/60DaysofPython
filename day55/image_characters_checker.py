# !pip install easyocr

import easyocr #identificar palavras(valores) dentro de uma imagem/ identify characters in images
import matplotlib.pyplot as plt
import cv2

#Select the image that you want 
# For Example:
caminho_da_imagem = "day55/Placa.jpg"

imagem = cv2.imread(caminho_da_imagem)
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

reader = easyocr.Reader(['en', 'pt']) #identifica as linguas da imagem
resultados = reader.readtext(imagem)

plt.imshow(imagem)
plt.axis("off")

for bbox, texto, confianca in resultados: #verificar a porcentagem de que algo está na imagem
  print(f"{texto} (confianca: {round(confianca * 100, 2)}% )")
