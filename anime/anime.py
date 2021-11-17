# Fichero que contiene al enumerado Genero y a la clase Anime

from aenum import Enum, NoAlias      #Biblioteca para que varios enum puedan tener los mismos valores sin problemas

class Genero(Enum):
    """
    Enumerado que encapsula los distintos géneros en que encuadrar un anime
    """

    _settings_= NoAlias

    ACTION = 40
    COMEDY = 30
    HORROR = 70
    SPORTS = 100
    ADVENTURE = 40
    DRAMA = 70
    MYSTERY = 70
    SUPERNATURAL = 50
    AVANTGARDE = 100
    FANTASY = 80
    ROMANCE = 70
    SUSPENSE = 60
    GIRLSLOVE = 100
    SCIFI = 70
    BOYSLOVE = 100
    SLIECEOFLIFE = 60


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

        '''
        Recalcula tanto la nota media como las visualizaciones después de que un usuario haya completado su visualización

        Parameters
        ----------
        nota: float
            Nota puesta por el usuario
        '''

    def recalcula_media(self, nota):
        self.puntuacion_media = ((self.puntuacion_media*self.visualizaciones+nota)/(self.visualizaciones+1))
        self.visualizaciones += 1