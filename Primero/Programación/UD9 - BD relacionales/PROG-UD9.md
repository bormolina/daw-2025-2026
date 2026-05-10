# UD9 - Bases de datos relacionales desde Python

Hasta ahora hemos trabajado, en gran parte, por separado: por un lado, en el módulo de **Programación** hemos aprendido a pensar problemas, escribir código, usar estructuras de datos, funciones, clases y ficheros; por otro lado, en **Bases de Datos** se ha visto cómo organizar, guardar y consultar información de forma estructurada.

En esta unidad vamos a empezar a juntar lo aprendido en ambos módulos. La idea es que nuestros programas ya no trabajen solo con datos temporales o ficheros sueltos, sino que puedan conectarse a una base de datos relacional, guardar información, recuperarla, modificarla y borrarla cuando sea necesario.

Esto es un paso importante: ya vamos pudiendo hacer cosas serias. Todavía nos faltan algunas piezas, pero cada vez queda menos para poder construir una aplicación o una web real, con código, datos y una lógica que se parezca mucho más a lo que se usa fuera del aula.

## Intro a SQLite

Para empezar a trabajar con bases de datos relacionales desde Python vamos a usar **SQLite**.

SQLite es un sistema de base de datos sencillo, ligero y muy práctico para aprender. A diferencia de otros sistemas como MySQL, PostgreSQL o SQL Server, SQLite no necesita instalar ni configurar un servidor. La base de datos se guarda directamente en un archivo, normalmente con extensión `.db` o `.sqlite`.

Esto lo convierte en una herramienta ideal para empezar: podemos crear una base de datos, guardar información en tablas y hacer consultas SQL desde nuestros programas de Python sin tener que preparar una infraestructura compleja.

Aunque SQLite sea sencillo, no es un juguete. Se usa en aplicaciones reales, en móviles, en programas de escritorio, en navegadores y en muchos proyectos donde se necesita una base de datos local, rápida y fácil de transportar.

## Cómo conectar a una BD SQLite en Python

Python incluye de serie el módulo `sqlite3`, así que no necesitamos instalar ninguna librería externa para empezar a trabajar con SQLite.

Para conectarnos a una base de datos usamos la función `sqlite3.connect()`. Si el archivo de base de datos ya existe, Python se conectará a él. Si no existe, SQLite lo creará automáticamente.

```python
import sqlite3

conexion = sqlite3.connect("instituto.db")

conexion.close()
```

En este ejemplo se crea o se abre una base de datos llamada `instituto.db`. La variable `conexion` representa la conexión con la base de datos, y al final usamos `close()` para cerrarla cuando ya no la necesitamos.

### Ejemplo 1: comprobar la conexión

Vamos a crear un primer programa muy sencillo para comprobar que podemos conectarnos correctamente a una base de datos SQLite.

El archivo del ejemplo se llama `ejemplo1.py`:

```python
from pathlib import Path
import sqlite3

RUTA_BD = Path(__file__).parent / "ejemplo1.db"

conexion = None

try:
    conexion = sqlite3.connect(RUTA_BD)
    print("Conexion realizada correctamente.")
except sqlite3.Error as error:
    print(f"Ha habido un error al conectar con la base de datos: {error}")
finally:
    if conexion is not None:
        conexion.close()
```

En este caso, el programa intenta conectarse a una base de datos llamada `ejemplo1.db`. Como SQLite trabaja con archivos, si esa base de datos no existe todavía, se creará automáticamente.

Para asegurarnos de que la base de datos se crea siempre en la misma carpeta que el archivo `ejemplo1.py`, usamos `Path(__file__).parent`. De esta forma, el programa no depende de la carpeta desde la que lo ejecutemos.

La variable `conexion` empieza con el valor `None` para indicar que, al principio, todavía no hay ninguna conexión abierta.

El bloque `try` contiene el código que queremos intentar ejecutar. Si la conexión se realiza correctamente, se mostrará el mensaje `Conexion realizada correctamente.`.

El bloque `except` se ejecutará solo si se produce un error relacionado con SQLite. En ese caso, el programa mostrará un mensaje indicando que ha habido un problema y enseñará información sobre el error.

Por último, el bloque `finally` se ejecuta siempre, haya habido error o no. Dentro de él comprobamos si la conexión llegó a abrirse y, si es así, la cerramos con `conexion.close()`. Cerrar la conexión es importante para liberar recursos y evitar dejar la base de datos abierta innecesariamente.
