def armo_csv(dic_ordenado,nombre_archivo):
    if nombre_archivo == "fuente_unico.csv":
    
        with open (nombre_archivo,"a") as codigo:

            # codigo.write("Nombre de la funcion Parametros formales Nombre del modulo")

            for clave in dic_ordenado:

                nombre_funcion = clave[0]
                parametros = clave[1][0]
                modulo = clave[1][1]
                cuerpo = clave[1][2]

                funcion = ", ".join(cuerpo)

                # codigo.write(nombre_funcion+",\t\t\t\t\t\t"+parametros+",\t\t\t\t"+modulo+",\n\n"+"Cuerpo de la funcion:\n\n"+funcion+"\n\n")

                codigo.write(nombre_funcion+","+parametros+","+modulo+","+funcion+"\n")

                """codigo.write(nombre_funcion+","+parametros+","+modulo+","+"\n\n"+funcion+"\n\n") ESTE LO CARGA MAS LIMPIO"""
    elif nombre_archivo == "comentarios.csv":
          with open (nombre_archivo,"a") as codigo:
                for clave in dic_ordenado:
                    nombre_funcion = clave[0]
                    autor = clave[1][0]
                    ayuda = clave[1][1]
                    cuerpo = clave[1][2]
                    funcion = ", ".join(cuerpo)

                    # codigo.write(nombre_funcion+",\t\t\t\t\t\t"+parametros+",\t\t\t\t"+modulo+",\n\n"+"Cuerpo de la funcion:\n\n"+funcion+"\n\n")

                    codigo.write(nombre_funcion+","+autor+","+ayuda+","+funcion+"\n")
                    

                    

                    
    else:
        print("Como llegamos aca. Ayuda")
