import random

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

ruta = "/home/carlos/Desktop/"


def matrixGen(rows, columns):
    print("\nGenerando matriz de 500x600")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(random.randint(0, 255))
        matrix.append(row)
    matrix = np.array(matrix)
    return matrix


def guardarImagen(matrix, nombre):
    print(f"\tGuardando imagen: {nombre}")
    im = Image.fromarray(matrix.astype(np.uint8))
    im.save(f'{ruta}{nombre}.jpg')
    # print("\tImagen guardada")


def generarHistograma(matrix):
    print("\tGenerando histograma")
    temp = np.hstack(matrix)
    plt.hist(temp, bins='auto')
    plt.title("Histograma de frecuencias")
    plt.savefig(f'{ruta}histogram.jpg')


def normalizarMatriz(matrix):
    temp = matrix.copy()
    print("\tNormalizando la matriz")
    for i in range(500):
        for j in range(600):
            if temp[i][j] < 128:
                temp[i][j] = 0
            else:
                temp[i][j] = 1
    return temp


def adyacencia4():
    '''
    rows, columns = matrix.shape
    for i in range(rows):
        for j in range(columns):
            if matrix[0][0] == 0:
                pass
            if matrix[]
    '''
    # No sé que hace, pero funciona
    matrix = np.random.randint(4, 8, (500, 600, 3))

    # Scale the values of the matrix between 0 and 255
    matrix = matrix / 10 * 255

    matrix = matrix.astype(np.uint8)

    # Convert the numpy array to a PIL Image object
    img = Image.fromarray(matrix, 'RGB')

    # Save the image to a file
    img.save(f'{ruta}aColor.png')


def filtrar(matrix, filtro):
    print("Original: \n", matrix)
    temp = []
    filtrado = matrix.copy()
    alto = len(matrix)
    ancho = len(matrix[0])
    for i in range(alto):
        for j in range(ancho):
            # print("\tactual: ", matrix[i][j], f"\t({i}, {j})")
            for k in range(-1, 2):
                if i - 1 < 0 or j + k > ancho - 1 or j + k < 0:
                    temp.append(0)
                else:
                    temp.append(matrix[i - 1][j + k])
            for k in range(-1, 2):
                if j + k < 0 or j + k > ancho - 1:
                    temp.append(0)
                else:
                    temp.append(matrix[i][j + k])
            for k in range(-1, 2):
                if j + k < 0 or j + k > ancho - 1 or i + 1 > alto - 1:
                    temp.append(0)
                else:
                    temp.append(matrix[i + 1][j + k])
            # print("temp: ", temp)
            product = list(np.multiply(filtro, temp))
            # print("producto: ", product)
            result = sum(product)
            # print("resultado: ", result)
            if result < 0:
                result = 0
            if result > 255:
                result = 255
            filtrado[i][j] = result
            temp = []
    print("Filtrada: \n", filtrado)
    return filtrado


def main():
    """1. Genera la matriz con valores aleatorios"""
    matrix = matrixGen(rows=500, columns=600)
    # print(type(matrix))
    # print(len(matrix[0]))

    """2. Guardar la imagen en formato jpg"""
    guardarImagen(matrix, 'grayScale')

    """3. Obtener el histograma de frecuencias"""
    generarHistograma(matrix)
    # print("\tHistograma guardado")

    """4. Binarizar la matriz"""
    matrixB = normalizarMatriz(matrix)
    print("\tMatriz normalizada")

    """5. Guardar la imagen de la nueva matriz"""
    guardarImagen((matrixB * 255).astype(np.uint8), "binarizada")

    """6. Etiquetado de componentes conectadas"""
    adyacencia4()
    # """7. Guarda la imagen a color"""
    # img = Image.fromarray(matrix, 'RGB')
    # img.save('/home/carlos/Desktop/image2.png')

    """7. Filtrados"""
    """     7.1 Filtro pasa altas"""
    filtro = [-1, -1, -1,
              -1, 9, -1,
              -1, -1, -1]
    filtrado = filtrar(matrix, filtro)
    guardarImagen(filtrado, "PasaAltas")

    """     7.2 Filtro estadístico: media"""
    filtro = [1, 1, 1,
              1, 1, 1,
              1, 1, 1]
    filtro = [i * 1 / 9 for i in filtro]
    filtrado = filtrar(matrix, filtro)
    guardarImagen(filtrado, "Media")


if __name__ == '__main__':
    main()
    """
    matrix = cv2.imread("/home/carlos/Downloads/test.png", cv2.IMREAD_GRAYSCALE)
    filtro = [1, 1, 1,
              1, 1, 1,
              1, 1, 1]
    filtro = [i * 1 / 9 for i in filtro]
    filtrado = filtrar(matrix, filtro)
    guardarImagen(filtrado, "Media")
    """
