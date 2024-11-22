import numpy as np
from PIL import Image

#cargar la imagen
imagen=Image.open("imagen.jpg")
imagen_np=np.array(imagen)

#crear un array para la escala de grises
alto, ancho, _ = imagen_np.shape
imagen_grises = np.zeros((alto, ancho), dtype=np.uint8)

#aplicar la formula
for y in range(alto):
    for x in range(ancho):
        r, g, b = imagen_np[y, x]
        gris = int(r*0.2989+g*0.5870+b*0.1140)
        imagen_grises[y, x]=gris

#Convertir el array de grises de vuelta a una imagen y mostrarla
imagen_grises = Image.fromarray(imagen_grises)
imagen_grises.show()