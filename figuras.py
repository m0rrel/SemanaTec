import pandas as pd
import math


df = pd.read_csv("figuras.csv", delim_whitespace=True)
print("El archivo ha sido leido")

def area_perimetro(figura, m1, m2):
    if figura == 'c':
        area = math.pi * m1**2
        perimetro = 2 * math.pi * m1
    elif figura == 'r':
        area = m1 * m2
        perimetro = 2 * (m1 + m2)
    elif figura == 't':
        area = (m1 * m2) / 2
        perimetro = m1 + m2 + math.hypot(m1, m2)
    else:
        area = perimetro = None
    return area, perimetro

for index, row in df.iterrows():
    figura = row['FIGURA']
    m1 = float(row['MEDIDA1'])
    m2 = float(row['MEDIDA2'])
    area, perimetro = area_perimetro(figura, m1, m2)
    print(f"Fila {index}: FIGURA={figura}, MEDIDA1={m1}, MEDIDA2={m2}, AREA={area:.2f}, PERIMETRO={perimetro:.2f}")

