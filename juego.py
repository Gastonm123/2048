from __future__ import print_function
from random import randint
import numpy as np

class Juego:
    def __init__(self):
        self.tablero = np.array([[0 for i in range(4)] for j in range(4)])
        self.state = True
        self.win = False
        self.score = 0
        self.putPiece()

    def putPiece(self):
        posLibres = []

        for i, linea in enumerate(self.tablero):
            for j, pieza in enumerate(linea):
                if pieza == 0:
                    posLibres.append((i, j))

        if len(posLibres) == 0:
            self.state = False
        else:
            pick = posLibres[ randint(0, len(posLibres)-1) ]
            ficha = 2 * randint(1, 2)

            self.tablero[pick[0]][pick[1]] = ficha
            self.score += ficha

    def moveLeft(self):
        #primero colapso las piezas iguales
        tablero = self.tablero.copy()

        for linea in self.tablero:
            anterior = 0
            for j, pieza in enumerate(linea):
                if pieza == 0:
                    pass
                elif anterior == 0:
                    anterior = (j, pieza)
                elif anterior[1] == pieza:
                    linea[j] = 0
                    linea[anterior[0]] = 2 * pieza
                    self.score += linea[anterior[0]]
                    anterior = 0
                else:
                    anterior = (j, pieza)

        #muevo las piezas
        for linea in self.tablero:
            piezas = [0 for i in range(4)]
            cont = 0

            for pieza in linea:
                if pieza == 0:
                    pass
                else:
                    piezas[cont] = pieza
                    cont += 1

            for i, pieza in enumerate(piezas):
                linea[i] = pieza

        if not np.array_equal(self.tablero, tablero):
            self.putPiece()

    def moveRigth(self):
        tablero = self.tablero.copy()

        for linea in self.tablero:
            anterior = 0
            for j, pieza in reversed(list(enumerate(linea))):
                if pieza == 0:
                    pass
                elif anterior == 0:
                    anterior = (j, pieza)
                elif anterior[1] == pieza:
                    linea[j] = 0
                    linea[anterior[0]] = 2 * pieza
                    self.score += linea[anterior[0]]
                    anterior = 0
                else:
                    anterior = (j, pieza)

        #muevo las piezas
        for linea in self.tablero:
            piezas = [0 for i in range(4)]
            cont = 3

            for pieza in reversed(linea):
                if pieza == 0:
                    pass
                else:
                    piezas[cont] = pieza
                    cont -= 1

            for i, pieza in enumerate(piezas):
                linea[i] = pieza

        if not np.array_equal(self.tablero, tablero):
            self.putPiece()

    def moveUp(self):
        #primero colapso las piezas iguales
        tablero = self.tablero.copy()

        for linea in self.tablero.T:
            anterior = 0
            for j, pieza in enumerate(linea):
                if pieza == 0:
                    pass
                elif anterior == 0:
                    anterior = (j, pieza)
                elif anterior[1] == pieza:
                    linea[j] = 0
                    linea[anterior[0]] = 2 * pieza
                    self.score += linea[anterior[0]]
                    anterior = 0
                else:
                    anterior = (j, pieza)

        #muevo las piezas
        for linea in self.tablero.T:
            piezas = [0 for i in range(4)]
            cont = 0

            for pieza in linea:
                if pieza == 0:
                    pass
                else:
                    piezas[cont] = pieza
                    cont += 1

            for i, pieza in enumerate(piezas):
                linea[i] = pieza

        if not np.array_equal(self.tablero, tablero):
            self.putPiece()

    def moveDown(self):
        tablero = self.tablero.copy()

        for linea in self.tablero.T:
            anterior = 0
            for j, pieza in reversed(list(enumerate(linea))):
                if pieza == 0:
                    pass
                elif anterior == 0:
                    anterior = (j, pieza)
                elif anterior[1] == pieza:
                    linea[j] = 0
                    linea[anterior[0]] = 2 * pieza
                    self.score += linea[anterior[0]]
                    anterior = 0
                else:
                    anterior = (j, pieza)

        #muevo las piezas
        for linea in self.tablero.T:
            piezas = [0 for i in range(4)]
            cont = 3

            for pieza in reversed(linea):
                if pieza == 0:
                    pass
                else:
                    piezas[cont] = pieza
                    cont -= 1

            for i, pieza in enumerate(piezas):
                linea[i] = pieza

        if not np.array_equal(self.tablero, tablero):
            self.putPiece()

    def show(self):
        for linea in self.tablero:
            for pieza in linea:
                print(pieza, end=", ")
            print('')
        