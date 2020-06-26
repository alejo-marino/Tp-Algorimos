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
                    print(linea,modulo)
                                   
            print(lineas)
leer_py(txt)
