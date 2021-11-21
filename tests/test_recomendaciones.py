import pytest
import sys
sys.path.append('./')
sys.path.append('./anime/')
from anime.usuario import Usuario
from anime.anime import Genero, Anime
from anime.recomendacion import recomienda




animes = [
Anime(0, "Shingeki no Kyojin", "Mundo ficticio en donde la humanidad está al borde de la extinción a causa de unas criaturas humanoides llamadas «titanes», por lo que los sobrevivientes se resguardan en tres enormes murallas que impiden el acceso a los monstruos.", "Tetsurou Araki", "Wit Studio", "Hajime Ishayama", 2013, 25, 24, [Genero.ACTION, Genero.DRAMA, Genero.MYSTERY, Genero.FANTASY], ["Netflix", "Amazon Prime"], 1567,8.52),
Anime(1, "Death Note", "Light Yagami, un estudiante de preparatoria, encuentra un cuaderno con poderes sobrenaturales llamado «Death Note», con el cual es capaz de matar personas si se escriben los nombres de estas en él, a la vez que si el portador visualiza mentalmente la cara de quien quiere asesinar.", "Tetsurou Araki", "Madhouse", "Tsugumi Ohba", 2006, 37, 23, [Genero.SUPERNATURAL, Genero.SUSPENSE, Genero.MYSTERY], ["Netflix"], 1844, 8.63),
Anime(2, "Hunter x Hunter", "Gon Freecss, un niño de doce años que desea encontrar a su padre a toda costa, decide convertirse en «cazador», justo como él, y de alguna forma hallar su paradero.", "Hiroshi Koujina", "Madhouse", "Yoshihiro Togashi", 2011, 148, 23, [Genero.ACTION, Genero.ADVENTURE, Genero.FANTASY], ["Crunchyroll"], 1231, 9.06),
Anime(3, "Haikyuu!!!", "Un hecho fortuito desencadena el amor de Shouyou Hinata por el voleibol. Su club no tenía ningún miembro, pero de algún modo perseveró y finalmente realizó su primer y último partido regular de la escuela secundaria, donde fue aniquilado por Tobio Kageyama, un jugador superestrella conocido como 'Rey de la Corte.'.", "Susumu Mitsunaka", "Production I.G.", "Haruichi Furudate", 2014, 25, 24, [Genero.SPORTS, Genero.COMEDY, Genero.DRAMA], ["Netflix"], 981, 8.46),
Anime(4, "Platinum End", "Mientras sus compañeros celebran su graduación, el joven y atormentado Mirai se encuentra con un ángel. Mirai ha sido elegido junto con otras 12 personas para una batalla en la que el ganador se convertirá en el nuevo Dios.", "Kazuchika Kise", "Signal.MD", "Tsugumi Ohba", 2021, 24, 24, [Genero.DRAMA, Genero.SUPERNATURAL], ["Crunchyroll"], 615, 7.25),
Anime(5, "Tokyo Ghoul", "Kaneki Ken termina convirtiéndose en un ser híbrido humano-ghoul y de ahora en adelante deberá vivir escondiéndose de los humanos.", "Shuuhei Morita", "Studio Pierrot", "Sui Ishida", 2014, 12, 24, [Genero.DRAMA, Genero.SUPERNATURAL, Genero.ACTION, Genero.MYSTERY, Genero.HORROR], ["Netflix"], 1201, 7.80),
Anime(6, "Akame ga Kill", "Tatsumi es un chico de campo que llega a la capital del Imperio para alistarse en el ejército. Debido a una serie de acontecimientos deberá enfrentarse a un grupo de sicarios conocido como Night Raid, pero la capital esconde secretos que Tatsumi jamás podría imaginar...", "Tomoki Kobayashi", "White Fox", "Takahiro", 2014, 24, 23, [Genero.DRAMA, Genero.FANTASY, Genero.ACTION, Genero.ADVENTURE], ["Netflix"], 897, 7.48),
Anime(7, "Shigatsu wa Kimi no Uso", "Un chico, prodigio del piano, que no puede escuchar su música después de haber sufrido un trauma en el cual perdió a su madre y a su instructor de piano. Habiéndole sido arrebatadas ambas personas, la vida de Kousei Arima se torna monótona y sin sentido. Un día le presentan a una violinista llamada Kaori Miyazono. A pesar de que su primera impresión de ella es terrible, la música de Kaori lo atrapa por completo.", "Kyouhei Ishiguro", "A-1 Pictures", "Naoshi Arakawa", 2014, 22, 22, [Genero.DRAMA, Genero.ROMANCE], ["Netflix"], 1176, 8.68),
Anime(8, "Neon Genesis Evangelion", "La organización NERV revela su nuevo proyecto con miras a salvar el mundo: gigantes y bio-mecánicos robots conocidos como Evas, que son unos de las pocas fuerzas sobre la Tierra capaces de enfrentar a los 'Ángeles'. Sólo niños específicos pueden pilotar los Evas: Shinji Ikari, el hijo de el jefe de NERV y que no desea pelear, la reservada Rei Ayanami y la exaltada (y algo amante del combate) Asuka Langley. Mientras combaten a los 'Ángeles' uno a uno, van descubriendo más y más acerca de la naturaleza y el futuro de la humanidad.", "Hideaki Anno", "Gainax", "Hideaki Anno", 1995, 26, 24, [Genero.DRAMA, Genero.ACTION, Genero.SCIFI, Genero.AVANT_GARDE], ["Netflix"], 815, 8.33)
]

user = Usuario("danifm13")


def test_vistos_vacio():
    assert len(user.vistos) == 0

def test_recomendaciones_vacio():
    assert len(user.recomendaciones) == 0

def test_recomienda_drama():
    recomendaciones = recomienda(user, animes, [Genero.DRAMA])
    assert len(recomendaciones) == 5                #Se han realizado 5 recomendaciones

def test_actualiza_recomendaciones_usuario():
    assert len(user.recomendaciones) > 0

def test_nota_mayor():
    mayor = True
    
    #Es necesario iterar en todos los elementos menos en el ultimo, y comparar con el siguiente elemento del array, lo que he encontrado es que esta es la mejor forma de hacerlo
    for i in range(len(user.recomendaciones)-1):
        if animes[user.recomendaciones[i]].puntuacion_media < animes[user.recomendaciones[i+1]].puntuacion_media:
            mayor = False
            break

    assert mayor                                 #Al hacer una busqueda por un solo genero recomienda el que tenga mayor nota con ese genero

def test_genero_presente():

    presente = False

    for rec in user.recomendaciones:
        presente = False
        for gen in animes[rec].generos:
            if gen == Genero.DRAMA:
                presente = True
                break

            if not presente:
                break

    assert presente                             #En todas las recomendaciones está el género deseado

def test_recomienda_girslove():
    recomendaciones = recomienda(user, animes, [Genero.GIRLS_LOVE])
    assert len(recomendaciones) == 0       #No hay actualmente animes con ese género, las recomendaciones deberían ser 0

def test_recomienda_horror():
    recomendaciones = recomienda(user, animes, [Genero.HORROR])
    assert len(recomendaciones) == 1       #Solo hay un anime con ese género

def test_recomienda_episodios_23():
    recomendaciones = recomienda(user, animes, [Genero.DRAMA], 23)
    assert len(recomendaciones) == 2        #Hay dos animes dramáticos con 23 capítulos o menos

def test_recomienda_episodios_10():
    recomendaciones = recomienda(user, animes, [Genero.ROMANCE], 12)
    assert len(recomendaciones) == 0        #No hay animes románticos de 12 capitulos o menos

def test_recomienda_varios_generos():
    recomendaciones = recomienda(user, animes, [Genero.ACTION, Genero.MYSTERY])
    assert len(recomendaciones) == 5        #Buscando por varios géneros da 5 resultados