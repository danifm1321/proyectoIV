import pytest
import sys
sys.path.append('./')
sys.path.append('./anime/')
from anime.usuario import Usuario
from anime.anime import Genero, Anime

anime1 = Anime(0, 
"Shingeki no Kyojin", 
"Mundo ficticio en donde la humanidad está al borde de la extinción a causa de unas criaturas humanoides llamadas «titanes», por lo que los sobrevivientes se resguardan en tres enormes murallas que impiden el acceso a los monstruos.",
"Tetsurou Araki",
"Wit Studio",
"Hajime Ishayama",
2013,
25,
24,
[Genero.ACTION, Genero.DRAMA, Genero.MYSTERY, Genero.FANTASY],
["Netflix", "Amazon Prime"],
1567,
8.52
)

anime2 = Anime(1,
"Death Note", 
"Light Yagami, un estudiante de preparatoria, encuentra un cuaderno con poderes sobrenaturales llamado «Death Note», con el cual es capaz de matar personas si se escriben los nombres de estas en él, a la vez que si el portador visualiza mentalmente la cara de quien quiere asesinar.",
"Tetsurou Araki",
"Madhouse",
"Tsugumi Ohba",
2006,
37,
23,
[Genero.SUPERNATURAL, Genero.SUSPENSE, Genero.MYSTERY],
["Netflix"],
1844,
8.63
)

user = Usuario("danifm13", "admin")

@pytest.fixture
def test_vistos_vacio():
    assert len(user.vistos) == 0

def test_historial_vacio():
    assert len(user.recomendaciones) == 0

def test_aniade_recom_nuevo():
    user.aniade_recom(anime1)
    assert user.recomendaciones.count(anime1.id) == 1

def test_aniade_recom_repetido():
    user.aniade_recom(anime1)
    assert user.recomendaciones.count(anime1.id) == 1

def test_aniade_visto_success():
    user.aniade_visto(anime2, 8)
    assert user.vistos.count((anime2.id, 8)) == 1

def test_anime_recom_fail():
    with pytest.raises(TypeError):
       user.aniade_recom(anime2)

def test_anime_visto_fail():
    with pytest.raises(TypeError):
        user.aniade_visto(anime2, 6)

