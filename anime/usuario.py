# Fichero que contiene la clase Usuario
from .anime import *

class Usuario:

    '''
    Clase que representa a un usuario
    
    Argumentos
    ----------
    usuario: str
        Nombre de usuario
    contrasena: str
        Contraseña del usuario
    visto: list[(int, float)]
        Historial de animes vistos por el usuario
    recomendaciones: list[int]
        Historial de recomendaciones realizadas al usuario
    '''

    def __init__(self, usuario, contrasena, vistos, recomendaciones):

        '''
        Construye objeto Usuario proporcionando valores para todos sus atributos

        Argumentos
        ----------
        usuario: str
            Nombre de usuario
        contrasena: str
            Contraseña del usuario
        visto: list[(int, float)]
            Historial de animes vistos por el usuario
        recomendaciones: list[int]
            Historial de recomendaciones realizadas al usuario
        '''

        self.usuario = usuario
        self.contrasena = contrasena
        self.vistos = vistos
        self.recomendaciones = recomendaciones
    

        