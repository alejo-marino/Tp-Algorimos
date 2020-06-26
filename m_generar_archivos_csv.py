txt = 'programas.txt'


def leer(archivo):
    with open(archivo) as f:
        lineas = [linea.rstrip('\n') for linea in f]
        return lineas

def test(aaa):
    pass
    return None



def leer_py(archivo):
        modulos = leer(archivo)
        for modulo in modulos:
            lineas = leer(modulo)
            for linea in lineas:
                  
                if linea.startswith('def '):
                    funcion = linea
                    index_inicial = lineas.index(funcion) +1
                    nombre_funcion = funcion.split('def ')[1].lstrip().split('(')[0]
                    parametros = funcion.split('(')[1].lstrip().split(')')[0]
                     
                elif linea.strip().startswith('return'):
                    linea_return = linea
                    index_final = lineas.index(linea_return) + 1
                    cuerpo = lineas[index_inicial:index_final]
                    return nombre_funcion,parametros,modulo,cuerpo
                   
leer_py(txt)
