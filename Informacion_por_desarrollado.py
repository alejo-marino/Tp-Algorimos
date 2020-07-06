import muestro_salida

def participacion_info (informacion):
    
    """[Autor: c]"""
    """[Ayuda: abre un archivo]"""

    autor_anterior = None
    total_funciones = 0
    muestro_salida.impresiones("\tInforme de Desarrollo Por Autor")

    for indice in range(len(informacion)-1):     
        
        autor, nombre_funcion, lineas_funcion, porcentaje = informacion[indice]

        total_funciones += 1

        if autor_anterior == None:

            muestro_salida.impresiones("Autor: " + autor +"\n\tFuncion\tLineas\n\t---------------------------------\n")
            
            contador_funciones = 0

            contador_lineas = 0

        elif autor_anterior!=autor:
            
            muestro_salida.impresiones(contador_funciones," Funciones - Lineas\t", contador_lineas,"  ",porcentaje)
            
            muestro_salida.impresiones("Autor: " + autor +"\n\tFuncion\tLineas\n\t---------------------------------\n")
            
            contador_funciones = 0

            contador_lineas = 0

        elif indice == len(informacion)-1 :
            
            muestro_salida.impresiones("\n\nTotal: ",contador_funciones,"Funciones - lineas\t",contador_lineas)

        else:
           
            muestro_salida.impresiones("\t" + nombre_funcion + "\t", lineas_funcion, "\n")

        
        contador_lineas += int(lineas_funcion)

        contador_funciones += 1

        autor_anterior = autor    





participacion_info()