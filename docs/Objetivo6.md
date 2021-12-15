## Elección del sistema de integración continua

Para nuestro sistema de integraición continua tenemos dos requisitos básicos: que sea compatible con github, nuestra plataforma de control de versiones, y que sea en la nube, es decir, online.

Consideremos usar github actions. Github es capaz de analizar nuestro código y recomendar worklows en base a nuestro lenguaje de programación y los frameworks que usemos. Además, contamos con [documentacion oficial de Github](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python) para añadir integración continua a nuestro proyecto de python haciendo uso de las github actions. 

También consideraremos usar CircleCI. CircleCI funciona sin plugins externos, y podemos definir un archivo yml que lea cada vez que realicemos el push. Además tiene su propio validador de yaml que nos facilita la creación del archivo de configuración.

Semaphore CI también es una sólida opción, para al darse de alta en la aplicación observamos que únicamente hay una prueba gratuita de 15 días, por lo tanto es descartado.

Se han tenido en cuenta Jenkins y TeamCity, dos herramientas de integración continua muy potentes. Sobre todo TeamCity, ya que tiene una versión gratuita con una interfaz visual bastante atractiva y clara.

Al final, me he decantado por CircleCI, ya que es el que me parece mas sencillo, ya que con un solo archivo de configuración tenemos nuestros tests preparados para ser evaluados.
