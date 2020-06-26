def leer_txt():
    with open('programas.txt') as f:
        modulos = [linea.rstrip('\n') for linea in f]
        return modulos
        
def leer_py(mod):
    for modulos in mod:
        with open(modulos) as f:
            modulos = [linea.rstrip('\n') for linea in f]
            for lineas in modulos:
                if lineas.startswith('def'):
                    print(lineas)
                   
        print(modulos)
                                 
leer_py(leer_txt())

