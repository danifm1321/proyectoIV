#Fichero que contiene el algoritmo de recomendacion
from anime import *
from usuario import *

'''
Función para ordenar el vector de recomendaciones por ponderación (mejor ponderación a peor)

Parameters
----------
recom : pair(Anime, float)
    Tupla de recomendación del anime con su ponderación

Returns
-------
recom[1] : float
    Ponderación del anime
'''
def sort_func(recom):
    return recom[1]

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
            ponderacion = 0
            for gen in ani.generos:
                if generos.count(gen) > 0:
                    ponderacion += gen.value
            
            if ponderacion > 0 and (num_episodios == None or ani.capitulos <= num_episodios):
                ponderacion *= ani.puntuacion_media
                recom.append((ani, ponderacion))
        
        recom.sort(key=sort_func)
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