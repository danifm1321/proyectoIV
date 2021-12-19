# anirec

El mundo de la animación japonesa, o anime, en lo que respecta tanto a películas como a series está creciendo a un ritmo enorme en estos últimos años en occidente.

Es por ello que podría ser útil una aplicación que recomiende este tipo de series al usuario adaptándose a sus gustos y proporcionandole información útil como dónde puede ver el contenido de manera legal.

## Instalación

Para comenzar debemos instalar nuestro gestor de dependencias [Poetry](docs/Objetivo3.md). Para instalarlo usamos la orden que se nos proporciona en la [documentacion oficial](https://python-poetry.org/docs/) de Poetry.

```shell
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

Para comprobar si se ha instalado correctamente realizamos:

```shell
poetry --version
```

En el directorio raíz del repositorio debemos realizar la siguiente orden para que Poetry instale todas las dependencias que necesita el proyecto para funcionar:

```shell
poetry install
```

Por último, debemos abrir el entorno virtual de poetry mediante:
```shell
poetry shell
```

Y una vez en el entorno podemos ver la lista de tareas definidas con:
```shell 
invoke --list
```

Ya podemos comprobar que la sintaxis de nuestro proyecto funciona correctamente con 
```shell
invoke check
```

Podemos lanzar los tests de nuestro proyecto con 
```shell
invoke test
```

## Documentación
- [Documentacion correspondiente al objetivo 1](docs/Objetivo1.md)
- [Documentacion correspondiente al objetivo 2](docs/Objetivo2.md)
- [Documentacion correspondiente al objetivo 3](docs/Objetivo3.md)
- [Documentacion correspondiente al objetivo 4](docs/Objetivo4.md)
- [Documentacion correspondiente al objetivo 5](docs/Objetivo5.md)
- [Documentacion correspondiente al objetivo 6](docs/Objetivo6.md)