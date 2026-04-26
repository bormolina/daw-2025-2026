<?xml version="1.0" encoding="UTF-8"?>

<!--
    Hoja de estilos XSLT.
    Sirve para transformar el documento XML de países en un documento HTML.
-->
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <!--
        Indicamos que la salida será HTML.
        - method="html": genera un documento HTML
        - encoding="UTF-8": codificación de salida
        - indent="yes": intenta dejar el resultado bien tabulado
    -->
    <xsl:output method="html" encoding="UTF-8" indent="yes"/>

    <!--
        Esta plantilla se aplica al nodo raíz del documento.
        Es decir, arranca la transformación desde el principio del XML.
    -->
    <xsl:template match="/">

        <!--
            A partir de aquí construimos directamente el HTML de salida.
            Todo lo que aparece como etiquetas normales HTML se copiará al resultado.
        -->
        <html>
            <head>
                <!--
                    Metadatos del documento HTML generado.
                -->
                <meta charset="UTF-8"/>
                <title>Países</title>
            </head>
            <body>
                <!--
                    Título principal de la página.
                -->
                <h1>Listado de países</h1>

                <!--
                    Creamos una tabla HTML para mostrar la información.
                    El atributo border="1" se usa solo para que se vea claramente.
                -->
                <table border="1">

                    <!--
                        Primera fila de la tabla: cabecera.
                        Aquí escribimos los nombres de las columnas.
                    -->
                    <tr>
                        <th>Nombre</th>
                        <th>Población</th>
                        <th>Área</th>
                        <th>Siglas</th>
                        <th>Capital</th>
                        <th>Habitantes de la capital</th>
                    </tr>

                    <!--
                        Recorremos todos los nodos <pais> que estén dentro de <paises>.
                        Por cada país encontrado, se generará una fila de la tabla.
                    -->
                    <xsl:for-each select="paises/pais">

                        <!--
                            Cada país genera una fila nueva.
                        -->
                        <tr>

                            <!--
                                xsl:value-of extrae el contenido de texto
                                del nodo indicado en select.
                            -->
                            <td>
                                <xsl:value-of select="nombre"/>
                            </td>

                            <td>
                                <xsl:value-of select="poblacion"/>
                            </td>

                            <td>
                                <xsl:value-of select="area"/>
                            </td>

                            <td>
                                <xsl:value-of select="siglas"/>
                            </td>

                            <!--
                                Aquí accedemos a nodos anidados.
                                capital/nombre significa:
                                dentro del nodo actual <pais>,
                                entra en <capital> y luego en <nombre>.
                            -->
                            <td>
                                <xsl:value-of select="capital/nombre"/>
                            </td>

                            <td>
                                <xsl:value-of select="capital/habitantes"/>
                            </td>
                        </tr>

                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>

</xsl:stylesheet>