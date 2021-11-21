#Fichero que contiene el algoritmo de recomendacion
from anime import *
from usuario import *


'''
Función que recomienda un anime en función a los géneros introducidos y el número de episodios

Parameters
----------
user : Usuario
    Usuario al que se va a realizar la recomendación
animes : list[Anime]
    Animes disponibles para realizar la recomendación
generos : list[Genero]
    Géneros seleccionados por el usuario para obtener la recomendación
num_episodios : float, optional
    Número de episodios máximos que quieres ver en un anime (por defecto es None)

Returns
-------
recomendaciones : list[Anime]
    Animes seleccionados como recomendación
'''
def recomienda(user, animes, generos, num_episodios = None):

    recomendaciones = []
    recom = []

    if len(user.vistos) == 0:

        for ani in animes:
            puntuacion = 0
            
            puntuacion = sum(map((lambda x : anime.ponderacion[x] if generos.count(x) > 0 else 0), ani.generos))

            if puntuacion > 0 and (num_episodios == None or ani.capitulos <= num_episodios):
                puntuacion *= ani.puntuacion_media
                recom.append((ani, puntuacion))
        
        recom.sort(key= lambda x : x[1])
        for rec in recom:
            recomendaciones.append(rec[0])
        
        recomendaciones.reverse()
        recomendaciones = recomendaciones[0:5]
    else:
        pass
        #No implementado todavia

    for reco in recomendaciones:
        user.aniade_recom(reco)

    return recomendaciones