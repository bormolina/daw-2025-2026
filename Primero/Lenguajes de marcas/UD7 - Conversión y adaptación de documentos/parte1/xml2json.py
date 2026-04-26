import xmltodict
import json
from pathlib import Path

ruta_xml = Path(__file__).parent / "paises.xml"
ruta_json = Path(__file__).parent / "paises.json"

with open(ruta_xml, "r", encoding="utf-8") as f:
    datos = xmltodict.parse(f.read())

with open(ruta_json, "w", encoding="utf-8") as f:
    json.dump(datos, f, ensure_ascii=False, indent=4)

print("Conversión completada")