## Contenedor: docker

Para la construcción del archivo update_docker.yml se ha seguido la [documentación oficial de github](https://docs.github.com/es/actions/publishing-packages/publishing-docker-images).

Para la elección de la imagen de python usada en el Dockerfile se han seguido las buenas práctica de la [documentación oficial de docker](https://docs.docker.com/language/python/build-images/)
La imagen a usar debe ser una imagen ligera que facilite el despliegue posterior de la aplicación. Por lo tanto, la imagen completa de python fue descartada, siendo demasiado pesada. En ese caso, -slim, que contiene lo mínimo para correr python, es una fuerte candidata. 
La otra imagen considerada como candidata sería -alpine, sin embargo -alpine es propenso a errores complicados de localizar y tiene mayores tiempos a la hora de construir la imagen.

En la construcción del docker usamos la siguiente orden: 
```shell
poetry config virtualenvs.create false
```

Debido a que con el uso de docker ya tenemos un entorno virtual, no es necesario crear el de poetry. Tras investigar acerca de la creación de Dockerfiles que incluyan poetry, he llegado a la conclusión de que no necesito para mi proyecto el entorno virtual de poetry.
La alternativa sería editar la variable de entorno $PATH global, no la perteneciente al entorno virtual de docker.