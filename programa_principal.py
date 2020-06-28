def leer_1(codigo):

    linea = codigo.readline()

    if linea:
        salida = linea.rstrip("\n")

    else:
        salida = ""

    return salida


