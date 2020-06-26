def leer(archivo):
    linea = archivo.readlines()

    if linea:
        devolver = linea.rstrip("\n").split(",")

    else:
        devolver = "","","",""
    
    return devolver
