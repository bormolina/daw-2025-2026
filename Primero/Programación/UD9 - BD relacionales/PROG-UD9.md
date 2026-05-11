
# UD9 - Bases de datos relacionales desde Python

[TOC]

## Introducción

Hasta ahora hemos trabajado, en gran parte, por separado: por un lado, en el módulo de **Programación** hemos aprendido a pensar problemas, escribir código, usar estructuras de datos, funciones, clases y ficheros; por otro lado, en **Bases de Datos** se ha visto cómo organizar, guardar y consultar información de forma estructurada.

En esta unidad vamos a empezar a juntar lo aprendido en ambos módulos. La idea es que nuestros programas ya no trabajen solo con datos temporales o ficheros sueltos, sino que puedan conectarse a una base de datos relacional, guardar información, recuperarla, modificarla y borrarla cuando sea necesario.

Esto es un paso importante: ya vamos pudiendo hacer cosas serias. Todavía nos faltan algunas piezas, pero cada vez queda menos para poder construir una aplicación o una web real, con código, datos y una lógica que se parezca mucho más a lo que se usa fuera del aula.

## SQLite

Para empezar a trabajar con bases de datos relacionales desde Python vamos a usar **SQLite**.

SQLite es un sistema de base de datos sencillo, ligero y muy práctico para aprender. A diferencia de otros sistemas como MySQL, PostgreSQL o SQL Server, SQLite no necesita instalar ni configurar un servidor. La base de datos se guarda directamente en un archivo, normalmente con extensión `.db` o `.sqlite`.

Esto lo convierte en una herramienta ideal para empezar: podemos crear una base de datos, guardar información en tablas y hacer consultas SQL desde nuestros programas de Python sin tener que preparar una infraestructura compleja.

Aunque SQLite sea sencillo, no es un juguete. Se usa en aplicaciones reales, en móviles, en programas de escritorio, en navegadores y en muchos proyectos donde se necesita una base de datos local, rápida y fácil de transportar.

<div style="page-break-after: always;"></div>

## Cómo conectar a una BD SQLite en Python

Python incluye de serie el módulo `sqlite3`, así que no necesitamos instalar ninguna librería externa para empezar a trabajar con SQLite.

Para conectarnos a una base de datos usamos la función `sqlite3.connect()`. Si el archivo de base de datos ya existe, Python se conectará a él. Si no existe, SQLite lo creará automáticamente.

```python
import sqlite3

conexion = sqlite3.connect("instituto.db")

conexion.close()
```

En este ejemplo se crea o se abre una base de datos llamada `instituto.db`. La variable `conexion` representa la conexión con la base de datos, y al final usamos `close()` para cerrarla cuando ya no la necesitamos.

<div style="page-break-after: always;"></div>

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

<div style="page-break-after: always;"></div>

## Conexión a una BD ya creada

En muchos casos, un programa no crea la base de datos desde cero. Lo más habitual es que la base de datos ya exista y que nuestro programa simplemente se conecte a ella para consultar, insertar, modificar o borrar información.

En esta unidad vamos a usar el fichero `games_db.py` para crear una base de datos de ejemplo llamada `games.db` y meter algunos datos iniciales. No hace falta comprender todavía todo el código de ese fichero, porque mezcla varias operaciones a la vez: crear tablas, insertar datos y relacionar información.

Lo que sí nos interesa entender es la **estructura** de la base de datos que genera.

### Tabla `usuarios`

La tabla `usuarios` guarda la información básica de cada usuario.

| Campo | Tipo | Restricciones | Explicación |
|---|---|---|---|
| `id` | `INTEGER` | `PRIMARY KEY AUTOINCREMENT` | Identificador único del usuario. SQLite lo genera automáticamente. |
| `nombre_usuario` | `TEXT` | `NOT NULL UNIQUE` | Nombre del usuario. Es obligatorio y no se puede repetir. |
| `email` | `TEXT` | `NOT NULL UNIQUE` | Correo del usuario. Es obligatorio y no se puede repetir. |
| `fecha_registro` | `TEXT` | `NOT NULL` | Fecha en la que se registró el usuario. |

### Tabla `juegos`

La tabla `juegos` guarda la información de los videojuegos.

| Campo | Tipo | Restricciones | Explicación |
|---|---|---|---|
| `id` | `INTEGER` | `PRIMARY KEY AUTOINCREMENT` | Identificador único del juego. |
| `titulo` | `TEXT` | `NOT NULL UNIQUE` | Título del juego. Es obligatorio y no se puede repetir. |
| `genero` | `TEXT` | `NOT NULL` | Género principal del juego. |
| `precio` | `REAL` | `NOT NULL CHECK (precio >= 0)` | Precio del juego. No puede ser negativo. |
| `fecha_lanzamiento` | `TEXT` |  | Fecha de lanzamiento del juego. |

### Tabla `usuarios_juegos`

La tabla `usuarios_juegos` es una tabla intermedia. Sirve para relacionar usuarios con juegos.

Esto es necesario porque un usuario puede tener muchos juegos, y un mismo juego puede pertenecer a muchos usuarios.

| Campo | Tipo | Restricciones | Explicación |
|---|---|---|---|
| `usuario_id` | `INTEGER` | `NOT NULL`, `FOREIGN KEY` | Identificador del usuario relacionado. |
| `juego_id` | `INTEGER` | `NOT NULL`, `FOREIGN KEY` | Identificador del juego relacionado. |
| `fecha_compra` | `TEXT` | `NOT NULL` | Fecha en la que el usuario compró o añadió el juego. |
| `horas_jugadas` | `REAL` | `NOT NULL DEFAULT 0 CHECK (horas_jugadas >= 0)` | Número de horas jugadas. Empieza en 0 y no puede ser negativo. |
| `favorito` | `INTEGER` | `NOT NULL DEFAULT 0 CHECK (favorito IN (0, 1))` | Indica si el juego es favorito. En SQLite usamos `0` para no y `1` para sí. |

Además, esta tabla usa una clave primaria compuesta:

```sql
PRIMARY KEY (usuario_id, juego_id)
```

Esto evita que un mismo usuario tenga el mismo juego repetido dos veces.

También usa claves ajenas:

```sql
FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
FOREIGN KEY (juego_id) REFERENCES juegos(id)
```

Estas claves indican que `usuario_id` debe corresponderse con un usuario existente, y que `juego_id` debe corresponderse con un juego existente.

### Consultar una base de datos desde Python

En el fichero `ejemplo2.py` tenemos un ejemplo de cómo conectarnos a una base de datos ya creada y realizar consultas sobre ella.

El programa muestra una lista de usuarios con su id y su nombre. Después, si escribimos el id de un usuario, muestra los juegos asociados a ese usuario. Si escribimos `0`, el programa termina.

Para ejecutar el ejemplo:

```bash
python ejemplo2.py
```

En este ejemplo aparecen tres métodos importantes:

```python
cursor = conexion.cursor()
```

`cursor()` crea un cursor. El cursor es el objeto que usamos para enviar consultas SQL a la base de datos y recoger sus resultados.

```python
cursor.execute("""
    SELECT id, nombre_usuario
    FROM usuarios
    ORDER BY id
""")
```

`execute()` ejecuta una sentencia SQL. En este caso ejecuta un `SELECT`, es decir, una consulta para leer datos.

Cuando una consulta necesita usar un dato que viene del usuario, no debemos pegar ese dato directamente dentro del texto SQL.

Por ejemplo, no deberíamos hacer esto:

```python
cursor.execute(f"SELECT * FROM usuarios WHERE id = {usuario_id}")
```

La forma correcta es usar `?` y pasar el valor aparte:

```python
cursor.execute("""
    SELECT *
    FROM usuarios
    WHERE id = ?
""", (usuario_id,))
```

El `?` indica el lugar donde irá el dato. SQLite se encarga de colocar ese valor de forma segura, tratándolo como un dato y no como parte del código SQL.

Esto es importante porque, si metemos directamente en el SQL texto escrito por el usuario, una persona podría escribir algo que modificase la consulta o provocase un error. A ese problema se le llama **inyección SQL**.

Además, cuando pasamos un solo valor, escribimos `(usuario_id,)` con coma final. Esa coma es necesaria para que Python cree una tupla de un solo elemento.



```python
usuarios = cursor.fetchall()
```

`fetchall()` recoge todas las filas devueltas por la consulta. En Python, el resultado es una lista de tuplas.

Por ejemplo, una consulta a la tabla `usuarios` podría devolver algo así:

```python
[
    (1, "maria99"),
    (2, "alex_dev"),
    (3, "samuel_22")
]
```

Cada tupla representa una fila de la tabla, y cada valor de la tupla corresponde a una columna del `SELECT`.

<div style="page-break-after: always;"></div>

## Crear CRUD

Un ejercicio muy habitual cuando empezamos a trabajar con bases de datos desde un programa es crear un **CRUD**.

CRUD son las siglas de:

| Letra | Operación | SQL habitual |
|---|---|---|
| C | Create, crear | `INSERT` |
| R | Read, leer | `SELECT` |
| U | Update, actualizar | `UPDATE` |
| D | Delete, borrar | `DELETE` |

Aunque el nombre pueda sonar un poco técnico, la idea es muy sencilla: hacer un programa que permita crear registros, consultarlos, modificarlos y borrarlos.

Este tipo de ejercicio es importante porque contiene casi todo lo necesario para aprender a gestionar una base de datos desde programación. Si sabemos hacer un CRUD sencillo, ya tenemos una base muy buena para construir aplicaciones más grandes.

Además, el curso que viene, en programación cliente-servidor, una parte importante será volver a hacer CRUD, pero esta vez desde aplicaciones web. La idea de fondo será la misma:

- mostrar datos;
- crear nuevos registros;
- modificar registros existentes;
- borrar registros.

La diferencia será que en vez de hacerlo desde consola, lo haremos desde una web, con formularios, rutas, peticiones HTTP y páginas HTML.

### Crear registros con `INSERT`

Para añadir datos a una tabla usamos `INSERT`.

Por ejemplo, en una tabla `stock` podríamos añadir un nuevo producto así:

```python
cursor.execute("""
    INSERT INTO stock (producto, categoria, precio)
    VALUES (?, ?, ?)
""", (producto, categoria, precio))

conexion.commit()
```

La sentencia SQL indica en qué tabla queremos insertar datos y qué columnas vamos a rellenar.

Los valores concretos se pasan aparte usando `?`. De esta forma evitamos construir SQL pegando strings y trabajamos de forma más segura.

Después del `INSERT` usamos `commit()` para confirmar los cambios. Si no hacemos `commit()`, los cambios pueden no quedar guardados definitivamente en la base de datos.

### Borrar registros con `DELETE`

Para borrar datos usamos `DELETE`.

Por ejemplo:

```python
cursor.execute("""
    DELETE FROM stock
    WHERE id = ?
""", (producto_id,))

conexion.commit()
```

La parte más importante es el `WHERE`. Sin `WHERE`, borraríamos todos los registros de la tabla.

Por eso, cuando borramos, normalmente usamos el `id` del registro que queremos eliminar.

### Modificar registros con `UPDATE`

Para modificar datos usamos `UPDATE`.

Por ejemplo:

```python
cursor.execute("""
    UPDATE stock
    SET producto = ?,
        categoria = ?,
        precio = ?
    WHERE id = ?
""", (nuevo_producto, nueva_categoria, nuevo_precio, producto_id))

conexion.commit()
```

Con `UPDATE` indicamos la tabla que queremos modificar, los campos que van a cambiar y el registro concreto sobre el que queremos actuar.

De nuevo, el `WHERE` es fundamental. Sin `WHERE`, modificaríamos todos los registros de la tabla.

### Lo importante

Fijaos en que aquí no aparece casi conocimiento nuevo de Python.

Seguimos usando cosas que ya conocemos:

- funciones;
- clases sencillas;
- `input()`;
- `print()`;
- bucles;
- condicionales;
- listas;
- objetos.

La parte nueva no es tanto Python, sino usar desde Python el SQL que ya conocemos:

- `SELECT` para leer;
- `INSERT` para crear;
- `UPDATE` para modificar;
- `DELETE` para borrar.

El programa `crud.py` es un ejemplo de esta idea aplicada a una tabla sencilla de productos de almacén.

<div style="page-break-after: always;"></div>

## Ejemplo de CRUD

El fichero `crud.py` contiene un CRUD sencillo sobre la base de datos `stock.db`.

Esta base de datos tiene una sola tabla, llamada `stock`, con productos de un almacén. Cada producto tiene:

- un `id`;
- un nombre de `producto`;
- una `categoria`;
- un `precio`.

El programa empieza conectándose a la base de datos:

```python
conexion = conectar()
```

Después entra en un bucle que se repite hasta que el usuario decide salir.

En cada vuelta del bucle, el programa muestra la lista de productos:

```txt
1 - Teclado mecanico
2 - Raton inalambrico
3 - Monitor 24 pulgadas
...
```

Después permite elegir una opción:

- escribir `C` para crear un producto nuevo;
- escribir un `id` para consultar un producto y, si queremos, modificarlo;
- escribir `-id` para borrar un producto;
- escribir `S` para salir.

### Crear

Cuando el usuario escribe `C`, el programa pide los datos del nuevo producto:

```txt
Producto:
Categoria:
Precio:
```

Después hace un `INSERT`:

```python
cursor.execute("""
    INSERT INTO stock (producto, categoria, precio)
    VALUES (?, ?, ?)
""", (producto, categoria, precio))
```

Con esto se crea una nueva fila en la tabla `stock`.

### Leer

Cuando el usuario escribe un número, el programa busca ese producto por su `id`:

```python
cursor.execute("""
    SELECT id, producto, categoria, precio
    FROM stock
    WHERE id = ?
""", (producto_id,))
```

Si existe, muestra sus datos por pantalla.

### Actualizar

Después de consultar un producto, el programa pregunta si queremos modificar algún dato.

Si respondemos que sí, nos pide los nuevos valores. Si dejamos un campo vacío, mantiene el valor anterior.

Después hace un `UPDATE`:

```python
cursor.execute("""
    UPDATE stock
    SET producto = ?,
        categoria = ?,
        precio = ?
    WHERE id = ?
""", (nuevo_nombre, nueva_categoria, nuevo_precio, producto.id))
```

### Borrar

Cuando el usuario escribe `-id`, el programa borra el producto con ese identificador.

Por ejemplo, `-3` borra el producto con id `3`.

La consulta que se ejecuta es:

```python
cursor.execute("""
    DELETE FROM stock
    WHERE id = ?
""", (producto_id,))
```

### Clase `Item`

En este ejemplo también aparece una clase sencilla llamada `Item`.

Esta clase representa un producto del almacén:

```python
class Item:
    def __init__(self, item_id: int, producto: str, categoria: str | None = None, precio: float | None = None) -> None:
        self.id = item_id
        self.producto = producto
        self.categoria = categoria
        self.precio = precio
```

Usar una clase nos permite trabajar con objetos en Python en lugar de manejar directamente tuplas todo el tiempo.

Por ejemplo, en vez de tener que recordar que una tupla tiene esta forma:

```python
(1, "Teclado mecanico", "Informatica", 49.99)
```

podemos usar atributos con nombre:

```python
producto.id
producto.producto
producto.categoria
producto.precio
```

Esto hace que el código sea más fácil de leer.

<div style="page-break-after: always;"></div>
