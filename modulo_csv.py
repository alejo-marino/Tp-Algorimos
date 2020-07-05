def armo_csv(dic_ordenado,nombre_archivo):
    """[Autor: F] """
    """[Ayuda: Hace cosas] """
    if nombre_archivo == "fuente_unico.csv":
        with open (nombre_archivo,"a") as codigo:

            for clave in dic_ordenado:
                #Modelo de parametros
                nombre_funcion = clave[0]
                parametros = clave[1][0]
                modulo = clave[1][1]
                cuerpo = clave[1][2]
                funcion = ", ".join(cuerpo)
                #Escribo en el csv
                codigo.write(nombre_funcion+","+parametros+","+modulo+","+funcion+"\n")
    elif nombre_archivo == "comentarios.csv":
          with open (nombre_archivo,"a") as codigo:
                for clave in dic_ordenado:
                    #Modelo de Parametros
                    nombre_funcion = clave[0]
                    autor = clave[1][0]
                    ayuda = clave[1][1]
                    cuerpo = clave[1][2]
                    funcion = ", ".join(cuerpo)
                    #Escribo en el csv
                    codigo.write(nombre_funcion+","+autor+","+ayuda+","+funcion+"\n")
    #Comedy relief       
    else:
        print("Como llegamos aca. Ayuda")