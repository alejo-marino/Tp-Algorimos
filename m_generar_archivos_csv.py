txt = 'programas.txt'

def leer(archivo):
    with open(archivo) as f:
        lineas = [linea.rstrip('\n') for linea in f]
        return lineas
        
def leer_py(archivo):
        modulos = leer(archivo)
        for modulo in modulos:
            lineas = leer(modulo)
            for linea in lineas:
                if linea.startswith('def '):
                    funcion = linea
                    nombre_funcion = funcion.split('def ')[1].lstrip().split('(')[0]
                    parametros = funcion.split('(')[1].lstrip().split(')')[0]
                    print(nombre_funcion,parametros,modulo)
                                   
           
leer_py(txt)
