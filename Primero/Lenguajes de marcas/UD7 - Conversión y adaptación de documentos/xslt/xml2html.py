from lxml import etree
from pathlib import Path

ruta_base = Path(__file__).parent
ruta_xml = ruta_base / "paises.xml"
ruta_xslt = ruta_base / "paises.xslt"
ruta_html = ruta_base / "paises.html"

# Cargar XML y XSLT
xml = etree.parse(str(ruta_xml))
xslt = etree.parse(str(ruta_xslt))

# Crear transformador
transformacion = etree.XSLT(xslt)

# Aplicar transformación
resultado = transformacion(xml)

# Guardar HTML generado
with open(ruta_html, "wb") as f:
    f.write(etree.tostring(resultado, pretty_print=True, encoding="UTF-8", method="html"))

print("Conversión completada: paises.html")