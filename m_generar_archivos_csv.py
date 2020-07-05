import modulo_csv

def leer(archivo):
    """[Autor: A]"""
    """El comenterario tiene que ser excluido """
    #OtroComment 
    #AAA
    """[Ayuda: Lee el archivo linea por linea]"""
    
    lineas = [linea.rstrip('\n') for linea in archivo]
    return lineas

def abro_ar(archivo):
    """[Autor: b]"""
    """[Ayuda: abre un archivo]"""
    
    with open(archivo) as archivo_completo:
        return leer(archivo_completo)

def ordenar_alfabeticamente(diccionario):
    """[Autor: b]"""
    """[Ayuda: abre un archivo]"""
    
    return sorted(diccionario.items(),key = lambda clave: clave[0], reverse = False)

def armar_csv_funciones(archivo):
    """[Autor: b]"""
    """[Ayuda: abre un archivo]"""

    datos = {}
    nombre_archivo = "fuente_unico.csv"
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
                armar_csv_comentarios(cuerpo,nombre_funcion)
                datos[nombre_funcion] = [parametros,modulo,cuerpo]

    funciones_alfabeto = ordenar_alfabeticamente(datos)

    return modulo_csv.armo_csv(funciones_alfabeto,nombre_archivo)

def armar_csv_comentarios(lista_cuerpo,nombre_funcion):
    """[Autor: D]"""
    """[Ayuda: Remueve los comentarios de la funcion y crea el archivo comentarios.csv]"""
    
    comentario_triple = '\"\"\"'
    nombre_archivo = 'comentarios.csv'
    datos_comentarios = {}
    lista = lista_cuerpo    
    for linea in lista:

        if linea.lstrip().startswith(comentario_triple) or linea.lstrip().startswith('#'):
            ind = lista_cuerpo.index(linea)
            k = lista_cuerpo.pop(ind)
            nombre_ayuda  = ""
            nombre_autor = ""
            cuerpo = ""
            if linea.lstrip().startswith(comentario_triple+"[Autor:"):
                linea_autor = linea
                nombre_autor = linea_autor.split('[Autor:')[1].lstrip().split(']')[0]

            elif linea.lstrip().startswith(comentario_triple+"[Ayuda:"):
                linea_ayuda = linea
                nombre_ayuda = linea_ayuda.split('[Ayuda:')[1].lstrip().split(']')[0]        
            else:
                cuerpo = [i for i in lista if (i.lstrip().startswith('#') or i.lstrip().startswith('#'))]
                datos_comentarios[nombre_funcion] = [nombre_autor,nombre_ayuda,cuerpo] 
        alfabetico = ordenar_alfabeticamente(datos_comentarios)
        return modulo_csv.armo_csv(alfabetico,nombre_archivo)       