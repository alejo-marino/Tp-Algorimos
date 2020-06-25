def leer_txt():
    with open("programas.txt") as f:
        lines = f.read().splitlines()
        return lines

def programas_a_analizar(lst):
    for i in lst:
        with open(i) as f:
            lines = f.read().splitlines()
            print(lines)    
            
programas_a_analizar(leer_txt())