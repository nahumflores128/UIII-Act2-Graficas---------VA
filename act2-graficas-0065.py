import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --- INICIO DEL PROGRAMA ---
print("=" * 60)
print("     INICIO DEL PROGRAMA - NAHUM FLORES 0065")
print("=" * 60)

# --- Datos de Autos (Marca, País Origen, Fabrica Eléctricos, Año Fundación) ---
toy = ['Toyota', 'Japón', True, 1937]
tsl = ['Tesla', 'EEUU', True, 2003]
bmw = ['BMW', 'Alemania', True, 1916]
ford = ['Ford', 'EEUU', True, 1903]  # Se usó 'ford' porque 'for' es palabra reservada
fer = ['Ferrari', 'Italia', True, 1939]

# Crear lista de listas y construir el DataFrame con Pandas
lista_autos = [toy, tsl, bmw, ford, fer]
df_autos = pd.DataFrame(lista_autos, columns=["Marca", "Pais_Origen", "Fabrica_Electricos", "Año_Fundacion"])

# Imprimir el DataFrame en consola con tu nombre
print("\n--- TABLA DE AUTOS | NAHUM FLORES 0065 ---")
print(df_autos)
print("-" * 60)

# Guardar DataFrame a un archivo CSV
df_autos.to_csv("autos.csv", index=False)

# 1. Gráfica de Línea
plt.plot(df_autos["Marca"], df_autos["Año_Fundacion"])
plt.title("Nahum Flores 0065 - Año de Fundación por Marca")
plt.xlabel("Marca de Auto")
plt.ylabel("Año de Fundación")
plt.show()

# 2. Gráfica de Dispersión (Scatter)
plt.scatter(df_autos["Marca"], df_autos["Año_Fundacion"])
plt.title("Nahum Flores 0065 - Dispersión - Año de Fundación")
plt.xlabel("Marca de Auto")
plt.ylabel("Año de Fundación")
plt.show()

# 3. Gráfica de Barras
plt.bar(df_autos["Marca"], df_autos["Año_Fundacion"])
plt.title("Nahum Flores 0065 - Año de Fundación por Marca")
plt.xlabel("Marcas")
plt.ylabel("Año de Fundación")
plt.show()

# 4. Ordenar gráfica de barras de manera descendente y aplicar colores
df_autos_ordenar = df_autos.sort_values("Año_Fundacion", ascending=False)
plt.bar(df_autos_ordenar["Marca"], df_autos_ordenar["Año_Fundacion"],
        color=["b", "g", "c", "m", "r"])
plt.title("Nahum Flores 0065 - Marcas Ordenadas (Descendente)")
plt.xlabel("Marcas")
plt.ylabel("Año de Fundación")
plt.show()

# 5. Gráfica de Pastel (Pie)
plt.pie(df_autos["Año_Fundacion"], labels=df_autos["Marca"], autopct='%1.1f%%')
plt.title("Nahum Flores 0065 - Distribución de Año de Fundación")
plt.show()

# --- FIN DEL PROGRAMA ---
print("\n" + "=" * 60)
print("     FIN DEL PROGRAMA - NAHUM FLORES 0065")
print("=" * 60)