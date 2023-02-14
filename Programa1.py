import random
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
    plt.title("Hisograma de frecuencias")
    plt.savefig(f'{ruta}histogram.jpg')


def normalizarMatriz(matrix):
    print("\tNormalizando la matriz")
    for i in range(500):
        for j in range(600):
            if matrix[i][j] < 128:
                matrix[i][j] = 0
            else:
                matrix[i][j] = 1
    return matrix


def adiacencia4():
    '''
    rows, columns = matrix.shape
    for i in range(rows):
        for j in range(columns):
            if matrix[0][0] == 0:
                pass
            if matrix[]
    '''
    # No se que hace, pero funciona
    matrix = np.random.randint(0, 10, (500, 600, 3))

    # Scale the values of the matrix between 0 and 255
    matrix = matrix / 10 * 255

    matrix = matrix.astype(np.uint8)

    # Convert the numpy array to a PIL Image object
    img = Image.fromarray(matrix, 'RGB')

    # Save the image to a file
    img.save(f'{ruta}aColor.png')


def main():
    """1. Geneara la matriz con valores aleatorios"""
    matrix = matrixGen(rows=500, columns=600)
    # print(type(matrix))
    # print(len(matrix[0]))

    """2. Guardar la imagen en formato jpg"""
    guardarImagen(matrix, 'grayScale')

    """3. Obtener el histograma de frecuencias"""
    generarHistograma(matrix)
    # print("\tHistograma guardado")

    """4. Binarizar la matriz"""
    matrix = normalizarMatriz(matrix)
    print("\tMatriz normalizada")

    """5. Guardar la imagen de la nueva matriz"""
    guardarImagen((matrix * 255).astype(np.uint8), "binarizada")

    """6. Etiquetado de componentes conectadas"""
    adiacencia4()
    # """7. Guarda la imagen a color"""
    # img = Image.fromarray(matrix, 'RGB')
    # img.save('/home/carlos/Desktop/image2.png')


if __name__ == '__main__':
    main()
