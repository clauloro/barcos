import sys
from random import shuffle, choice, random
from introducir import solicitar_introducir_si_o_no, solicitar_introducir_casilla


CASO_NO_JUGADO = chr(0x2610)
CASO_TOCADO = chr(0x2611)
CASO_AGUA = chr(0x2612)

HORIZONTAL = 0
VERTICAL = 1


class Casilla:
    def __init__(self, letra, numero):
        self.letra = letra
        self.numero = numero
        self.estado = CASO_NO_JUGADO
        self.barco = None
    
    def __str__(self):
        return self.estado
    
    def jugar(self):
        if self.barco:
            self.estado = CASO_TOCADO
            self.barco.casillas.remove(self)
        else:
            self.estado = CASO_AGUA
    

class Barco:
    def __init__(self, nombre, longitud):
        self.nombre = nombre
        self.longitud = longitud
        self.casillas = []
        self.orientacion = None
        
    def __str__(self):
        return self.nombre


class Tablero:
    def __init__(self):
        self.casillas = {}
        self.barcos = []
        
        # Crear las casillas del tablero
        for letra in 'ABCDEFGHIJ':
            for numero in range(1, 11):
                nombre_casilla = letra + str(numero)
                self.casillas[nombre_casilla] = Casilla(letra, numero)
