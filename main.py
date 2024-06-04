import itertools
import pandas as pd

def generar_tabla_sumas(dado1_caras, dado2_caras):
    if dado1_caras > dado2_caras:
        dado1_caras, dado2_caras = dado2_caras, dado1_caras
    
    # Crear una lista de resultados para cada dado
    resultados_dado1 = range(1, dado1_caras + 1)
    resultados_dado2 = range(1, dado2_caras + 1)
    
    # Crear una lista de listas para almacenar las sumas
    sumas = []
    for i in resultados_dado2:
        fila = []
        for j in resultados_dado1:
            fila.append(i + j)
        sumas.append(fila)
    
    # Crear el DataFrame con pandas
    df = pd.DataFrame(sumas, columns=[f'Dado 1: {i}' for i in resultados_dado1], index=[f'Dado 2: {i}' for i in resultados_dado2])
    
    return df

def calcular_probabilidades(df):
    # Calcular la probabilidad de que la suma sea 12
    total_combinaciones = df.size
    suma_12 = (df == 12).sum().sum()
    probabilidad_suma_12 = (suma_12 / total_combinaciones) * 100
    
    # Calcular la probabilidad de que el número sea par y mayor a 11
    pares_mayores_11 = ((df > 11) & (df % 2 == 0)).sum().sum()
    probabilidad_pares_mayores_11 = (pares_mayores_11 / total_combinaciones) * 100
    
    return probabilidad_suma_12, probabilidad_pares_mayores_11

def main():
    # Solicitar el número de caras de cada dado
    dado1_caras = int(input("Ingrese el número de caras del dado 1: "))
    dado2_caras = int(input("Ingrese el número de caras del dado 2: "))
    
    # Generar la tabla de sumas
    tabla_sumas = generar_tabla_sumas(dado1_caras, dado2_caras)
    
    # Mostrar la tabla
    print(tabla_sumas)
    
    # Calcular y mostrar las probabilidades
    probabilidad_suma_12, probabilidad_pares_mayores_11 = calcular_probabilidades(tabla_sumas)
    print(f"\nProbabilidad de que la suma sea 12: {probabilidad_suma_12:.4f}%")
    print(f"Probabilidad de obtener un número par mayor a 11: {probabilidad_pares_mayores_11:.4f}%")

if __name__ == "__main__":
    main()
