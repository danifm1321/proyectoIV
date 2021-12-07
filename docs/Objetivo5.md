## Contenedor: docker

Para la construcción del archivo update_docker.yml se ha seguido la [documentación oficial de github](https://docs.github.com/es/actions/publishing-packages/publishing-docker-images).

Para la elección de la imagen de python usada en el Dockerfile se han seguido las buenas práctica de la [documentación oficial de docker](https://docs.docker.com/language/python/build-images/)
La imagen a usar debe ser una imagen ligera que facilite el despliegue posterior de la aplicación. En ese caso, -slim contiene lo mínimo para correr python, lo cual la convierte en una fuerte candidata.
Otra imagen candidata sería alpine, sin embargo alpine es propenso a errores complicados de localizar.

En la construcción del docker usamos la siguiente orden: 
```shell
poetry config virtualenvs.create false
```

Debido a que con el uso de docker ya tenemos un entorno virtual, no es necesario crear el de poetry. Tras investigar acerca de la creación de Dockerfiles que incluyan poetry, he llegado a la conclusión de que no necesito para mi proyecto el entorno virtual de poetry.
La alternativa sería editar la variable de entorno $PATH global, no la perteneciente al entorno virtual de docker.