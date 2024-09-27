# Calculadora de Probabilidades para Dados

Este proyecto es un ejercicio universitario que calcula la probabilidad de ciertos resultados al lanzar dos dados de diferentes tamaños.

## Descripción

El programa permite al usuario especificar el número de caras para dos dados diferentes. Luego, genera una tabla de sumas posibles y calcula las siguientes probabilidades:

1. La probabilidad de que la suma de los dados sea 12.
2. La probabilidad de obtener un número par mayor a 11.

Este ejercicio fue diseñado específicamente para calcular estas probabilidades con dados de 6 y 12 caras, pero el código es flexible y permite usar dados con cualquier número de caras.

## Requisitos

- Python 3.x
- Pandas

## Instalación

1. Asegúrate de tener Python 3.x instalado en tu sistema.
2. Instala la biblioteca Pandas ejecutando:
   ```
   pip install pandas
   ```
3. Descarga el archivo `dados_probabilidad.py` de este repositorio.

## Uso

1. Ejecuta el script desde la línea de comandos:
   ```
   python dados_probabilidad.py
   ```
2. Sigue las instrucciones en pantalla para ingresar el número de caras para cada dado.
3. El programa mostrará la tabla de sumas posibles y las probabilidades calculadas.

## Ejemplo de salida

```
Ingrese el número de caras del dado 1: 6
Ingrese el número de caras del dado 2: 12

[Tabla de sumas]

Probabilidad de que la suma sea 12: X.XXXX%
Probabilidad de obtener un número par mayor a 11: X.XXXX%
```

## Estructura del código

- `generar_tabla_sumas(dado1_caras, dado2_caras)`: Genera una tabla de pandas con todas las sumas posibles.
- `calcular_probabilidades(df)`: Calcula las probabilidades requeridas.
- `main()`: Función principal que maneja la entrada del usuario y la salida de resultados.
