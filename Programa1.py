import random
import numpy as np
import matplotlib.pyplot as plt


def matrixGen(rows, columns):
    print("\nGenerando matriz de 500x600")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(random.randint(0, 255))
        matrix.append(row)
    matrix = np.array(matrix)
    print("\tMatriz generada")
    return matrix


def main():
    """1. Geneara la matriz con valores aleatorios"""
    matrix = matrixGen(rows=500, columns=600)
    print(type(matrix))

    """2. Guardar la imagen en formato jpg"""
    print("\tGuardando imagen")
    fig = plt.imshow(matrix, cmap='gray')
    plt.axis('off')
    plt.savefig('/home/carlos/Desktop/grayScale.jpg', bbox_inches='tight', pad_inches=0)
    print("\tImagen guardada")

    """3. Obtener el histograma de frecuencias"""
    plt.clf()
    print("\tGenerando histograma")
    temp = np.hstack(matrix)
    plt.hist(temp, bins='auto')
    plt.title("Hisograma de frecuencias")
    plt.savefig('/home/carlos/Desktop/histogram.jpg')
    print("\tHistograma guardado")

    """4. Binarizar la matriz"""
    print("\tNormalizando la matriz")

    print("\tMatriz normalizada")

    """5. Guardar la imagen de la nueva matriz"""
    print("\tGuardando imagen")

    print("\tImagen guardada")


if __name__ == '__main__':
    main()
