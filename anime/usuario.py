# Fichero que contiene la clase Usuario
from anime import *

class Usuario:

    '''
    Clase que representa a un usuario
    
    Attributes
    ----------
    usuario: str
        Nombre de usuario
    contrasena: str
        Contraseña del usuario
    visto: list[(int, float)]
        Historial de animes vistos por el usuario
    recomendaciones: list[int]
        Historial de recomendaciones realizadas al usuario
    
    Methods
    -------
    ha_visto(id)
        Comprueba si el usuario ha visto el anime introcido
    aniade_visto(anime, nota)
        Añade un anime a la lista de animes vistos por el usuario junto con su nota
    aniade_recom(anime)
        Añade un anime a la lista de animes recomendados al usuario
    '''

    def __init__(self, usuario, contrasena, vistos = [], recomendaciones = []):

        '''
        Construye objeto Usuario proporcionando valores para todos sus atributos

        Parameters
        ----------
        usuario: str
            Nombre de usuario
        contrasena: str
            Contraseña del usuario
        vistos: list[pair(int, int)]
            Lista de animes vistos por el usuario junto con su nota
        recomendaciones: list[int]
            Lista de animes recomendados al usuario
        '''

        self.usuario = usuario
        self.contrasena = contrasena
        self.vistos = vistos
        self.recomendaciones = recomendaciones
    
        '''
        Comprueba si el usuario ha visto el anime introcido

        Parameters
        ----------
        id : int
            Id del anime a comprobar
        
        Returns
        -------
        nuevo: boolean
            True si el usuario no ha visto el anime, False si sí
        '''

    def ha_visto(self, id):
        nuevo = True
        for ani in self.vistos:
            if ani[0] == id:
                nuevo = False
                break
        
        return nuevo

        '''
        Añade un anime a la lista de animes vistos por el usuario junto con su nota
     
        Parameters
        ----------
        anime : Anime
            Anime a introducir en la lista
        nota : float
            Nota a poner por el usuario para el anime
        
        Raises
        ------
        TypeError
            Si el anime ya está incluido en la lista
        '''
    def aniade_visto(self, anime, nota):

        if self.ha_visto(anime.id):
            pareja = (anime.id, nota)
            self.vistos.append(pareja)
            anime.recalcula_media(nota)
        else:
            raise TypeError("El anime ya está incluido")

        '''
        Añade un anime a la lista de animes recomendados al usuario

        Parameters
        ----------
        anime : Anime
            Anime a introducir en la lista de recomendaciones 
        
        Raises
        ------
        TypeError
            Si el anime se encuentra en la lista de vistos por el usuario
        '''
    def aniade_recom(self, anime):

        if self.ha_visto(anime.id):
            if self.recomendaciones.count(anime.id) == 0:
                self.recomendaciones.append(anime.id)
        else:
            raise TypeError("El usuario ya ha visto el anime")