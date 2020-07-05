import contar_funciones
txt = 'programas.txt'


def leer(archivo):
    
    """ El comenterario tiene que ser excluido """
    
    # El comenterario tiene que ser excluido

    lineas = [linea.rstrip('\n') for linea in archivo]
    
    return lineas


def abro_ar(archivo):
    
    with open(archivo) as archivo_completo:
        
        return leer(archivo_completo)

def remover_comentarios(lista_cuerpo,nombre_funcion):
    comentario_triple = "\"\"\""
    for i in lista_cuerpo:
        if i.strip().startswith("#") or i.strip().startswith(comentario_triple):
            j = lista_cuerpo.index(i)
            k = lista_cuerpo.pop(j)
            datos_comentarios[nombre_funcion] = [k]
            #TODO: Queda pasarlo a csv


def leer_py(archivo):
    import modulo_csv
    datos = {}
    modulos = abro_ar(archivo)
    for modulo in modulos:
        lineas = abro_ar(modulo)
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
                remover_comentarios(cuerpo,nombre_funcion)
                datos[nombre_funcion] = [parametros,modulo,cuerpo]

    funciones_alfabeto = sorted(datos.items(),key = lambda clave: clave[0], reverse = False)

    return modulo_csv.armo_csv(funciones_alfabeto)


def main():

    leer_py(txt)
    

    return None

main()