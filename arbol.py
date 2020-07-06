def cantidadDeLineas(funcion):
    contLineas = 0
    for linea in funcion:
        if linea:
            contLineas += 1
    return contLineas