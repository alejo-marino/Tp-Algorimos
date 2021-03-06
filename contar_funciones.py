def contar_funciones(linea):
    """[Autor : F] """
    cantidad_funciones = {"if": 0, "while": 0, "for": 0, "returns": 0, "break": 0, "exit": 0, "ayuda": 0}
    if linea.strip().startswith("if"):
        cantidad_funciones["if"] += 1
    elif linea.strip().startswith("while"):
        cantidad_funciones["while"] += 1
    elif linea.strip().startswith("for"):
        cantidad_funciones["for"] += 1
    elif linea.strip().startswith("return"):
        cantidad_funciones["returns"] += 1
    elif linea.strip().startswith("break"):
        cantidad_funciones["break"] += 1
    elif linea.strip().startswith("exit"):
        cantidad_funciones["exit"] += 1
    elif linea.strip().startswith("[Ayuda: ]"):
        cantidad_funciones["ayuda"] += 1
    return cantidad_funciones
