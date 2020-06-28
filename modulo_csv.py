def armo_csv(datos):
    
    nombre_funcion,parametros,modulo,cuerpo = datos
    
    with open ("fuente_unico.csv","a") as codigo:
        codigo.write("Nombre de la funcion \t\t Parametros formales \t\t Nombre del modulo")
        codigo.write("\n\t\t"+nombre_funcion)
        codigo.write(",\t\t\t\t\t\t"+parametros)
        codigo.write(",\t\t\t\t"+modulo+",\n\n")
        codigo.write("Cuerpo de la funcion:\n\n")
        funcion = "\n".join(cuerpo)
        codigo.write(funcion+"\n\n")
        """codigo.write(nombre_funcion+","+parametros+","+modulo+","+"\n\n"+funcion+"\n\n") ESTE LO CARGA MAS LIMPIO"""
        return None