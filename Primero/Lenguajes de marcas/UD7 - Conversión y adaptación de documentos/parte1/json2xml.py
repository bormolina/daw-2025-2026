import xmltodict
import json
from pathlib import Path

ruta_json = Path(__file__).parent / "paises.json"
ruta_xml = Path(__file__).parent / "paises2.xml"

with open(ruta_json, "r", encoding="utf-8") as f:
    datos = json.load(f)

xml_texto = xmltodict.unparse(datos, pretty=True)

with open(ruta_xml, "w", encoding="utf-8") as f:
    f.write(xml_texto)

print("Conversión completada")