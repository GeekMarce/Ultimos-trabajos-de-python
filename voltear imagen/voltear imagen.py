import numpy as np
from PIL import Image

#cargar la imagen y usar .convert("L") para convertirla a escala de grises
imagen=Image.open("imagen.jpg").convert("L")
imagen_np=np.array(imagen)

#obtener el alto y ancho de la imagen y hacer una copia para poder trabajar
#sin modificar la imagen original de la carpeta
alto, ancho=imagen_np.shape
imagen_volteada=np.copy(imagen_np)

#Voltear imagen manualmente
for y in range(alto): #recorre filas
    for x in range(ancho//2): #para que no recorra todo y se voltee bien
        IndOp=ancho-x-1 #calcula el índice opuesto
        aux=imagen_volteada[y, x] #guarda temporalmente el pixel para reemplazarlo
        imagen_volteada[y, x]=imagen_volteada[y, IndOp] #asigna el opuesto
        imagen_volteada[y, IndOp] = aux #restaura el valor guardado

#mostrar la imagen volteada
imagen_volteada = Image.fromarray(imagen_volteada)
imagen_volteada.show()