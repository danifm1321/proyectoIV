# Fichero que contiene la clase Usuario
from anime import *

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

    def __init__(self, usuario, contrasena, vistos = [], recomendaciones = []):

        '''
        Construye objeto Usuario proporcionando valores para todos sus atributos

        Argumentos
        ----------
        usuario: str
            Nombre de usuario
        contrasena: str
            Contraseña del usuario
        '''

        self.usuario = usuario
        self.contrasena = contrasena
        self.vistos = vistos
        self.recomendaciones = recomendaciones
    

    def aniade_visto(self, anime, nota):

        nuevo = True
        for ani in self.vistos:
            if ani[0] == anime.id:
                nuevo = False
                break

        if nuevo:
            pareja = (anime.id, nota)
            self.vistos.append(pareja)
            anime.recalcula_media(nota)
        else:
            raise TypeError("El anime ya está incluido")

    def aniade_recom(self, anime):

        nuevo = True
        for ani in self.vistos:
            if ani[0] == anime.id:
                nuevo = False
                break

        if nuevo:
            if self.recomendaciones.count(anime.id) == 0:
                self.recomendaciones.append(anime.id)
        else:
            raise TypeError("El usuario ya ha visto el anime")