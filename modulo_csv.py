def armo_csv(dic_ordenado):
    
    with open ("fuente_unico.csv","a") as codigo:
        
        for clave in dic_ordenado:
            
            nombre_funcion = clave[0]
            parametros = clave[1][0]
            modulo = clave[1][1]
            cuerpo = clave[1][2]

            codigo.write("Nombre de la funcion \t\t Parametros formales \t\t Nombre del modulo")
            codigo.write("\n\t\t"+nombre_funcion)
            codigo.write(",\t\t\t\t\t\t"+parametros)
            codigo.write(",\t\t\t\t"+modulo+",\n\n")
            codigo.write("Cuerpo de la funcion:\n\n")
            funcion = "\n".join(cuerpo)
            codigo.write(funcion+"\n\n")
            """codigo.write(nombre_funcion+","+parametros+","+modulo+","+"\n\n"+funcion+"\n\n") ESTE LO CARGA MAS LIMPIO"""
    
    return None