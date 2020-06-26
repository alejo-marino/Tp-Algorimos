def leer(archivo):
    linea = archivo.redlines():

    if linea:
        devolver = linea.rstrip("\n").split(",")

    else:
        devolver = "","","",""
    
    return linea