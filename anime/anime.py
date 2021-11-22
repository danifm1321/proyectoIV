# Fichero que contiene al enumerado Genero y a la clase Anime
from enum import Enum, auto



class Genero(Enum):
    """
    Enumerado que encapsula los distintos géneros en que encuadrar un anime
    """

    ACTION = auto()
    COMEDY = auto()
    HORROR = auto()
    SPORTS = auto()
    ADVENTURE = auto()
    DRAMA = auto()
    MYSTERY = auto()
    SUPERNATURAL = auto()
    AVANT_GARDE = auto()
    FANTASY = auto()
    ROMANCE = auto()
    SUSPENSE = auto()
    GIRLS_LOVE = auto()
    SCIFI = auto()
    BOYS_LOVE = auto()
    SLICE_OF_LIFE = auto()

ponderacion = {Genero.ACTION : 40, Genero.COMEDY : 30, Genero.HORROR : 70, Genero.SPORTS : 100, Genero.ADVENTURE : 40, Genero.DRAMA : 40, Genero.MYSTERY : 70, Genero.SUPERNATURAL : 50, Genero.AVANT_GARDE : 100, Genero.FANTASY : 80, Genero.ROMANCE : 70, Genero.SUSPENSE : 60, Genero.GIRLS_LOVE : 100, Genero.SCIFI : 70, Genero.BOYS_LOVE : 100, Genero.SLICE_OF_LIFE : 60}


class Anime:
    """
    Clase que representa a un anime.

    ...

    Attributes
    ---------
    id : str
        Cadena identificadora del Anime
    titulo : str 
        Título del Anime
    sinopsis : str 
        Sinopsis del Anime
    director : str 
        Director del Anime
    estudio : str 
        Estudio de animación en el que se ha desarrollado el anime
    creador : str 
        Creador de la obra original en caso de proceder de una obra previa
    anio : int 
        Año de estreno del Anime
    capitulos : int 
        Número de capítulos del Anime
    duracion_media : int 
        Duración media de capítulos en minutos
    generos : list[Genero] 
        Lista de los géneros en que puede encuadrarse el Anime
    plataformas : list[str] 
        Lista de plataformas en las que se puede ver el Anime de forma legal
    visualizaciones :  int 
        Número de visualizaciones del Anime
    puntuacion_media : float
        Puntuación media que los usuarios le han dado al Anime
    
    Methods
    -------
    recalcula_media(nota)
        Recalcula tanto la nota media como las visualizaciones después de que un usuario haya completado su visualización
    aniade_visualizacion()
        Añade una visualización al anime

    """

    def __init__(self, id, titulo, sinopsis, director, estudio, creador, anio, 
                capitulos, duracion_media, generos, plataformas, visualizaciones, 
                puntuacion_media):
        """
        Construye objeto Anime proporcionando valores para todos sus atributos

        Parameters
        ----------
            id : str
                Cadena identificadora del Anime
            titulo : str 
                Título del Anime
            sinopsis : str 
                Sinopsis del Anime
            director : str 
                Director del Anime
            estudio : str 
                Estudio de animación en el que se ha desarrollado el anime
            creador : str 
                Creador de la obra original en caso de proceder de una obra previa
            anio : int 
                Año de estreno del Anime
            capitulos : int 
                Número de capítulos del Anime
            duracion_media : int 
                Duración media de capítulos en minutos
            generos : list[Genero] 
                Lista de los géneros en que puede encuadrarse el Anime
            plataformas : list[str] 
                Lista de plataformas en las que se puede ver el Anime de forma legal
            visualizaciones :  int 
                Número de visualizaciones del Anime
            puntuacion_media : float
                Puntuación media que los usuarios le han dado al Anime
        """

        self.id = id
        self.titulo = titulo
        self.sinopsis = sinopsis
        self.director = director
        self.estudio = estudio
        self.creador = creador
        self.anio = anio
        self.capitulos = capitulos
        self.duracion_media = duracion_media
        self.generos = generos
        self.plataformas = plataformas
        self.visualizaciones = visualizaciones
        self.puntuacion_media = puntuacion_media



    def recalcula_media(self, nota):
        '''
        Recalcula tanto la nota media como las visualizaciones después de que un usuario haya completado su visualización

        Parameters
        ----------
        nota: float
            Nota puesta por el usuario
        '''
        self.puntuacion_media = ((self.puntuacion_media*self.visualizaciones+nota)/(self.visualizaciones+1))
       

    def aniade_visualizacion(self):
        '''
        Añade una visualización al anime
        '''
        self.visualizaciones += 1