import json
import os

def exportar_a_json(datos, nombre_archivo="quotes.json", carpeta="output"):
    if not datos:
        print("No hay datos para guardar.")
        return

    os.makedirs(carpeta, exist_ok=True)
    ruta = os.path.join(carpeta, nombre_archivo)

    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)

    print(f"Datos guardados en {ruta}")
