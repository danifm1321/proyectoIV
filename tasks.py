from invoke import task, run

@task
def check(c):
    '''
    Comprueba la sintaxis del programa
    '''
    print("Comprobando sintaxis...")
    run("pylint -E anime")

@task
def test(c):
    '''
    Realiza los tests necesarios para el correcto funcionamiento de la aplicacion
    '''
    print("Lanzando tests...")
    run("pytest")