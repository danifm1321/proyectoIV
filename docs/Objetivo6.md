## Elección del sistema de integración continua

Para nuestro sistema de integración continua tenemos dos requisitos básicos: que sea compatible con github, nuestra plataforma de control de versiones, y que sea en la nube, es decir, online. Dentro de esto, nuestra preferencia es que sea gratuito y sencillo de implementar en nuestro proyecto.

Consideremos usar github actions. Github es capaz de analizar nuestro código y recomendar worklows en base a nuestro lenguaje de programación y los frameworks que usemos. Además, contamos con [documentacion oficial de Github](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python) para añadir integración continua a nuestro proyecto de python haciendo uso de las github actions. 

También consideraremos usar CircleCI. CircleCI funciona sin plugins externos, y podemos definir un archivo yml que lea cada vez que realicemos el push. Además tiene su propio validador de yaml que nos facilita la creación del archivo de configuración.

Semaphore CI también es una sólida opción, para al darse de alta en la aplicación observamos que únicamente hay una prueba gratuita de 15 días, por lo tanto es descartado.

Se han tenido en cuenta Jenkins y TeamCity, dos herramientas de integración continua muy potentes. Sobre todo TeamCity, ya que tiene una versión gratuita con una interfaz visual bastante atractiva y clara. Para ambas es necesario una instalación para su uso, por lo que quedan descartadas ante alternativas que nos permiten una implementación más simple en el proyecto.

Al final, mi elección ha sido una Github Action que nos permita evaluar los tests cada vez que añadamos código nuevo, ya que la integración de la Github Action en nuestro proyecto es muy sencilla: simplemente un archivo en el directorio correspondiente. 

## Sistema para comprobar las versiones del lenguaje

Para el control de las versiones del lenguaje he usado CircleCI, ya que cuenta con unos entornos docker de los lenguajes de python que nos permiten testear las versiones fácilmente.

### Creación de config.yml

He usado la versión 2.1 de CircleCI ya que es la más actual.
He usado las imágenes de docker correspondientes a las versiones del lenguaje a testear. En un inicio, planteé utilizar el contenedor de la anterior práctica, pero se debería de construir un contenedor por versión a probar, lo cual no me pareció correcto, ya que no es nada escalable.
Sabemos que la función auto de Enum, usada en anime.py, solo funciona de python 3.6 en adelante, así que las versiones de python a ser candidatas son python 3.6, 3.7, 3.8, 3.9 y 3.10. Descartaremos python 3.8, ya que es la usada en el docker que se testea a través de la Github Action. Python 3.6 también será descartada ya que dejará de recibir [actualizaciones de seguridad](https://endoflife.date/python) a partir de 2022. Teniendo esto en cuenta, considero conveniente testear las versiones 3.7, 3.9 y 3.10 usando circle CI.
