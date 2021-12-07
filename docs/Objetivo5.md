## Contenedor: docker

Para la construcción del archivo update_docker.yml se ha seguido la [documentación oficial de github](https://docs.github.com/es/actions/publishing-packages/publishing-docker-images).

Para la elección de la imagen de python usada en el Dockerfile se han seguido las buenas práctica de la [documentación oficial de docker](https://docs.docker.com/language/python/build-images/)
La imagen a usar debe ser una imagen ligera que facilite el despliegue posterior de la aplicación. En ese caso, -slim contiene lo mínimo para correr python, lo cual la convierte en una fuerte candidata.
Otra imagen candidata sería alpine, sin embargo alpine es propenso a errores complicados de localizar.