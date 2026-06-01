# Instalación de Odoo con Docker

En esta práctica vamos a preparar el entorno necesario para ejecutar Odoo usando Docker.

Todavía no entraremos en la configuración interna de Odoo. El objetivo de esta primera parte es comprobar que Docker funciona correctamente y levantar los contenedores necesarios.

---

# Paso 1. Comprobar si Docker está instalado

Abre una terminal y ejecuta:

```bash
docker --version
```

Si Docker está instalado correctamente, debería aparecer una versión similar a:

```text
Docker version 28.x.x
```

También comprobaremos Docker Compose:

```bash
docker compose version
```

Si ambos comandos funcionan correctamente, puedes pasar directamente al **Paso 3**.

---

# Paso 2. Windows: comprobar WSL

Si estás en Windows, trabajaremos usando WSL (Windows Subsystem for Linux).

WSL permite ejecutar una distribución Linux dentro de Windows y será el entorno recomendado para trabajar con Docker.

Para comprobar si WSL está instalado, abre PowerShell y ejecuta:

```powershell
wsl -l -v
```

También puedes usar:

```powershell
wsl --list --verbose
```

Deberías ver algo similar a:

```text
  NAME      STATE           VERSION
* Ubuntu    Running         2
```

Lo importante es que la distribución esté en versión `2`.

Si no tienes WSL instalado, ejecuta:

```powershell
wsl --install
```

Después reinicia el equipo si Windows lo solicita.

A partir de este momento, todos los comandos se ejecutarán dentro de Ubuntu/WSL.

---

# Paso 2b. Instalar Docker CE en Linux o WSL

Si Docker no está instalado, crea un archivo llamado:

```text
instalar-docker.sh
```

Con el siguiente contenido:

```bash
#!/bin/bash

set -e

echo "Actualizando paquetes..."
sudo apt update

echo "Instalando dependencias necesarias..."
sudo apt install -y ca-certificates curl gnupg

echo "Creando directorio para claves..."
sudo install -m 0755 -d /etc/apt/keyrings

echo "Descargando clave GPG oficial de Docker..."
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
  sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo "Ajustando permisos de la clave..."
sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo "Añadiendo repositorio oficial de Docker..."
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

echo "Actualizando paquetes..."
sudo apt update

echo "Instalando Docker CE y Docker Compose..."
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

echo "Comprobando instalación..."
docker --version
docker compose version

echo "Añadiendo usuario actual al grupo docker..."
sudo usermod -aG docker "$USER"

echo "Instalación finalizada."
echo "IMPORTANTE: cierra sesión y vuelve a entrar para usar docker sin sudo."
```

Ejecuta el script:

```bash
bash instalar-docker.sh
```

Para comprobar que Docker funciona correctamente:

```bash
docker run hello-world
```

Si aparece un mensaje de bienvenida, Docker está funcionando correctamente.

---

# Paso 3. Crear el proyecto de Odoo

Vamos a crear una carpeta para el proyecto:

```bash
mkdir odoo-docker
cd odoo-docker
```

Dentro crearemos un archivo llamado:

```text
docker-compose.yml
```

Este archivo define los contenedores que necesita nuestra aplicación.

En este caso usaremos:

- un contenedor para Odoo
- un contenedor para PostgreSQL
- volúmenes para conservar los datos

Contenido del archivo:

```yaml
services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: postgres
      POSTGRES_USER: odoo
      POSTGRES_PASSWORD: odoo
    volumes:
      - odoo-db-data:/var/lib/postgresql/data

  odoo:
    image: odoo:18.0
    depends_on:
      - db
    ports:
      - "8069:8069"
    environment:
      HOST: db
      USER: odoo
      PASSWORD: odoo
      ADMIN_PASSWD: admin
    volumes:
      - odoo-web-data:/var/lib/odoo

volumes:
  odoo-db-data:
  odoo-web-data:
```

---

# Paso 4. Levantar los contenedores

Ejecuta:

```bash
docker compose up -d
```

La primera vez puede tardar porque Docker tiene que descargar las imágenes necesarias.

Cuando termine, comprueba el estado de los contenedores:

```bash
docker compose ps
```

Deberías ver los servicios `odoo` y `db` en ejecución.

---

# Paso 5. Comandos básicos de gestión

## Parar los contenedores

```bash
docker compose stop
```

Esto detiene los contenedores, pero no los elimina.

---

## Arrancar los contenedores detenidos

```bash
docker compose start
```

---

## Reiniciar los contenedores

```bash
docker compose restart
```

---

## Apagar y eliminar los contenedores

```bash
docker compose down
```

Este comando elimina los contenedores y la red creada por Docker Compose, pero conserva las imágenes y los volúmenes.

---

## Apagar y borrar también los volúmenes

```bash
docker compose down -v
```

Cuidado: este comando elimina también los volúmenes.

En este caso, se perderían los datos almacenados por PostgreSQL y Odoo.

---

# Resumen de comandos

```bash
docker --version
docker compose version
docker compose up -d
docker compose ps
docker compose stop
docker compose start
docker compose restart
docker compose down
docker compose down -v
```

---

# Paso 6. Instalación inicial de Odoo

Una vez levantados los contenedores, abre el navegador y entra en:

```text
http://localhost:8069
```

Aparecerá la pantalla inicial de creación de base de datos de Odoo.

Rellena los campos de la siguiente manera:

```text
Master Password: admin
Database Name: odoo
Email: odoo@odoo.es
Password: odoo
Phone number: se puede dejar vacío
Language: Spanish / Español
Country: Spain
Demo data: marcado
```

El campo `Email` puede ser falso, pero debes recordarlo, porque será el usuario con el que entrarás después en Odoo.

El campo `Password` será la contraseña de ese usuario. También debes recordarla.

Es importante marcar la opción:

```text
Demo data
```

Esto carga datos de ejemplo dentro de Odoo, como clientes, productos, ventas y facturas. Para esta práctica nos interesa tener datos de prueba, ya que así podremos explorar mejor la aplicación.

Después pulsa el botón para crear la base de datos.

El proceso puede tardar un poco.

Cuando termine, aparecerá la pantalla de login de Odoo.

Introduce:

```text
Usuario: el correo que hayas escrito
Contraseña: la contraseña que hayas elegido
```

Si todo ha ido correctamente, entrarás en el panel principal de administración de Odoo.

---

# Paso 7. Contextualización de la empresa

Antes de comenzar a usar Odoo, es importante entender el contexto de la empresa que vamos a gestionar.

En esta práctica trabajaremos con una empresa ficticia llamada:

```text
Borgasa
```

Borgasa es una empresa dedicada a ofrecer soluciones de digitalización para otras empresas, especialmente relacionadas con:

- inteligencia artificial
- automatización
- servicios cloud
- despliegue de aplicaciones
- modernización de infraestructuras

La empresa ofrece dos tipos principales de servicios:

## Packs genéricos

Son servicios baratos y muy estandarizados.

Por ejemplo:

- creación básica de página web
- despliegue de WordPress
- chatbot sencillo
- automatización básica
- hosting básico

Estos packs permiten conseguir muchos clientes rápidamente, aunque dejan poco margen económico.

---

## Soluciones personalizadas

Son proyectos adaptados a cada empresa.

Por ejemplo:

- automatizaciones específicas
- despliegues cloud complejos
- integración de IA
- paneles personalizados
- análisis de datos

Aquí es donde realmente la empresa obtiene la mayor parte de sus beneficios.

---

# Configuración inicial de la empresa

Ahora vamos a configurar la información básica de Borgasa (o la empresa que tu hayas pensado).

Ve a:

```text
Settings / Ajustes → Companies / Compañías
```

Entra en la empresa principal y modifica los datos básicos.

Por ejemplo:

```text
Nombre: Borgasa
País: España
Teléfono: 600000000
Email: contacto@borgasa.local
Sitio web: https://borgasa.local
```

También puedes añadir:

- logotipo
- dirección
- CIF ficticio
- descripción

---

# Paso 8. Instalación de aplicaciones

Odoo funciona mediante módulos o aplicaciones.

Cada aplicación añade funcionalidades concretas al sistema.

Por ejemplo:

- gestión de clientes
- ventas
- inventario
- contabilidad
- recursos humanos
- tienda online
- marketing

Una empresa no tiene por qué usar todos los módulos. Lo normal es instalar únicamente aquellos que realmente necesita.

---

## Aplicaciones mínimas recomendadas

Para esta práctica instalaremos únicamente tres aplicaciones básicas:

```text
CRM
Ventas
Contactos
```

Estas aplicaciones suelen ser las mínimas en muchas empresas porque permiten gestionar:

- clientes
- presupuestos
- pedidos

Sin entrar todavía en partes más complejas como:

- contabilidad
- inventario avanzado
- recursos humanos

---

## ¿Qué hace cada aplicación?

### CRM

El módulo CRM permite gestionar posibles clientes y oportunidades comerciales.

Sirve para:

- registrar empresas interesadas
- hacer seguimiento comercial
- controlar negociaciones

Por ejemplo:

```text
Cliente interesado
↓
Presupuesto enviado
↓
Negociación
↓
Venta conseguida
```

---

### Ventas

El módulo Ventas permite gestionar ventas reales.

Sirve para:

- crear presupuestos
- generar pedidos
- gestionar productos
- generar documentos PDF
- controlar ventas realizadas

---

### Contactos

El módulo Contactos permite almacenar información de clientes y empresas.

Sirve para:

- guardar clientes
- teléfonos
- correos
- direcciones
- información comercial

Muchas aplicaciones de Odoo utilizan internamente el sistema de contactos.

---

## Cómo instalar aplicaciones

Ve a:

```text
Apps
```

En el buscador superior escribe:

```text
CRM
```

Y pulsa:

```text
Install
```

Haz lo mismo con:

```text
Sales
Contacts (aunque está suele estar activada por defecto porque la usan casi todos los demás módulos)
```

La instalación (o activación) puede tardar unos segundos.

Una vez instaladas (o activadas), aparecerán en el menú principal de Odoo.

### Nota
Después de instalar las aplicaciones, es normal que aparezcan:

- notificaciones
- tareas pendientes
- actividades
- ventas
- oportunidades comerciales
- mensajes
- clientes ya creados

Esto ocurre porque durante la instalación marcamos la opción:

```text
Load Demonstration Data
```

Odoo ha cargado automáticamente datos de ejemplo para facilitar las pruebas y exploración de la aplicación.

Estos datos no son reales y pueden ignorarse o eliminarse más adelante si se desea.

---

# Paso 9. Usuarios y acceso seguro a la información

En una empresa real no todos los trabajadores necesitan acceder a toda la información.

Dependiendo de su puesto, cada empleado tendrá acceso únicamente a las partes del sistema necesarias para realizar su trabajo.

Esto permite:

- proteger información sensible
- evitar errores
- limitar accesos innecesarios
- mejorar la seguridad del sistema

---

## Contexto de Borgasa

En Borgasa vamos a trabajar con dos empleados ficticios.

### Juan — Comercial

Juan trabaja en el departamento comercial.

Su trabajo consiste en:

- contactar con clientes
- negociar presupuestos
- realizar seguimiento de ventas
- preparar propuestas comerciales

Juan necesita acceder al módulo de ventas para gestionar presupuestos y pedidos, pero no necesita acceder a la parte de contabilidad o facturación de la empresa.

Por ello tendrá acceso únicamente al módulo:

```text
Ventas
```

---

### María — Administración y contabilidad

María trabaja en administración.

Su trabajo consiste principalmente en:

- revisar ventas
- gestionar facturas
- controlar documentación
- supervisar pagos y contabilidad

María sí necesita acceder tanto a ventas como a contabilidad.

Por ello tendrá acceso a:

```text
Ventas
Contabilidad
```

---

## Crear usuarios

Ve a:

```text
Settings / Ajustes → Users & Companies → Users
```

Y crea los siguientes usuarios:

```text
juan@borgasa.local
maria@borgasa.local
```

Puedes usar cualquier contraseña sencilla para la práctica.

---

## Configurar permisos

### Juan

Asigna:

```text
Sales - Ventas → User
Accounting - Contabilidad → Nada
```

El resto no le des acceso (por defecto no lo tendrá).

---

### María

Asigna:

```text
Sales - Ventas → User
Accounting - Contabilidad → Administrator
```

El resto no le des acceso (por defecto no lo tendrá).

---

## Asignar contraseña

Una vez creado cada usuario, debes asignarle una contraseña.

Para ello:

- entra en el usuario
- pulsa el icono del engranaje situado arriba a la izquierda
- selecciona la opción para cambiar la contraseña

Puedes usar contraseñas sencillas para la práctica.

Por ejemplo:

```text
juan123
maria123
```

---

## Verificación

Una vez creados los usuarios:

- cierra sesión
- entra con cada usuario
- observa qué módulos aparecen
- comprueba que Juan solo tiene acceso a ventas
- comprueba que María tiene acceso a ventas y contabilidad


---

# Paso 10. Generación de informes

Uno de los usos más habituales de un ERP es la generación automática de documentos empresariales.

En este caso vamos a generar un presupuesto en PDF utilizando el módulo de ventas.

---

## Crear un presupuesto

Ve a:

```text
Ventas → Pedidos → Presupuestos
```

Pulsa:

```text
Nuevo
```

Selecciona:

- un cliente
- uno o varios productos
- cantidad

Puedes utilizar los datos de demostración cargados por Odoo o crear productos propios relacionados con Borgasa.

Por ejemplo:

```text
Producto: Automatización básica IA
Cantidad: 1
```

Guarda el presupuesto.

---

## Generar informe del presupuesto 

Una vez creado el presupuesto, pulsa:

```text
Vista previa
```

Odoo generará automáticamente una vista del documento empresarial.

Después, desde el navegador, puedes:

```text
Imprimir → Guardar como PDF
```

o descargar directamente el PDF si el navegador lo permite.

---

# Paso 11. Extracción de información

Los sistemas ERP permiten exportar información para:

- analizar datos
- generar informes externos
- trabajar con hojas de cálculo
- importar datos en otros sistemas

En este ejercicio vamos a exportar información de clientes en formato CSV.

---

## Exportar contactos

Ve a:

```text
Contactos
```

Cambia a:

```text
Modo lista
```

Selecciona varios contactos utilizando las casillas situadas a la izquierda.

Después pulsa:

```text
Acción → Exportar
```

Selecciona algunos campos sencillos, por ejemplo:

```text
Nombre
Correo electrónico
Teléfono
País
```

Y exporta el resultado en formato:

```text
CSV
```

---

## Resultado

Odoo generará automáticamente un archivo CSV con la información seleccionada.

Este fichero puede utilizarse posteriormente en:

- Excel
- LibreOffice Calc
- otras aplicaciones empresariales
- procesos de análisis de datos
- sistemas externos

---

# Material a entregar

El alumno deberá demostrar durante la corrección que Odoo funciona correctamente en su equipo.

Durante la defensa de la práctica se podrá pedir:

- arrancar y detener los contenedores Docker
- comprobar el estado de los contenedores
- acceder a Odoo como administrador
- acceder con el perfil de Juan (ventas)
- acceder con el perfil de María (ventas y contabilidad)
- crear presupuestos
- generar documentos PDF
- generar nuevos usuarios
- exportar información en formato CSV

---

## Documentación

Además de la demostración práctica, el alumno deberá entregar un documento donde explique el proceso seguido durante la práctica.

El documento debe incluir:

- explicación breve de los pasos realizados
- comandos utilizados
- configuración realizada
- usuarios creados
- presupuestos generados
- exportaciones realizadas
- capturas de pantalla

---

### Formato del documento

El documento debe:

- ir directo al grano pero explicar suficientemente el proceso
- estar bien estructurado
- incluir títulos y apartados claros

Las capturas de pantalla deben:

- verse correctamente
- tener tamaño suficiente
- poder leerse sin necesidad de hacer zoom
- mostrar claramente la información relevante

---

### Entrega

Un documento de texto de Google Classroom

Que deberá contener:

- documentación
- capturas utilizadas

# Rúbrica

## Odoo funcionando correctamente (15 puntos)

- **15 puntos** — Odoo funciona correctamente y el alumno demuestra soltura y eficacia durante la ejecución.
- **10 puntos** — Odoo funciona correctamente, aunque el alumno necesita ayuda puntual o muestra cierta inseguridad.
- **5 puntos** — Odoo funciona parcialmente o con bastantes problemas, pero existe una instalación mínimamente funcional.
- **0 puntos** — La instalación no funciona, no puede demostrarse o la entrega carece de sentido.

---

## Gestión de contenedores Docker (15 puntos)

- **15 puntos** — El alumno sabe arrancar, detener y comprobar contenedores con soltura y eficacia.
- **10 puntos** — El alumno consigue realizar las operaciones principales, aunque con dudas o lentitud.
- **5 puntos** — El alumno consigue realizar alguna operación básica con bastante ayuda.
- **0 puntos** — El alumno no sabe gestionar los contenedores o la entrega carece de sentido.

---

## Acceso con distintos perfiles (15 puntos)

- **15 puntos** — Accede correctamente y con soltura a todos los perfiles solicitados comprendiendo sus diferencias.
- **10 puntos** — Accede correctamente a la mayoría de perfiles, aunque con pequeñas dudas o errores menores.
- **5 puntos** — Solo consigue acceder parcialmente o existe una configuración muy limitada de permisos.
- **0 puntos** — No existen perfiles diferenciados funcionales o la entrega carece de sentido.

---

## Generación de nuevos usuarios (5 puntos)

- **5 puntos** — Genera usuarios correctamente y comprende cómo asignar permisos.
- **0 puntos** — No sabe crear usuarios o la configuración no tiene sentido.

---

## Generación de presupuestos (15 puntos)

- **15 puntos** — Genera presupuestos correctamente y con soltura usando datos coherentes.
- **10 puntos** — Genera presupuestos funcionales, aunque con errores menores o poca soltura.
- **5 puntos** — Genera un presupuesto muy básico o parcialmente incorrecto, pero funcional.
- **0 puntos** — No consigue generar presupuestos funcionales o la entrega carece de sentido.

---

## Generación de informes/PDF (15 puntos)

- **15 puntos** — Genera informes correctamente y comprende el proceso completo de generación de documentación.
- **10 puntos** — Genera informes funcionales, aunque con dudas o pequeños fallos menores.
- **5 puntos** — Genera parcialmente el informe o el resultado presenta bastantes problemas.
- **0 puntos** — No consigue generar informes o la entrega carece de sentido.

---

## Exportación de contactos CSV (15 puntos)

- **15 puntos** — Exporta correctamente la información comprendiendo el proceso y el formato generado.
- **10 puntos** — Exporta correctamente aunque con inseguridad o pequeños errores menores.
- **5 puntos** — Realiza parcialmente la exportación o el fichero generado presenta problemas importantes.
- **0 puntos** — No consigue exportar información o la entrega carece de sentido.

---

## Documentación (20 puntos)

- **20 puntos** — Documento muy claro, bien estructurado, directo al grano, con encabezados claros y capturas perfectamente visibles.
- **15 puntos** — Documento correcto y entendible, aunque con algunos problemas menores de estructura o capturas.
- **10 puntos** — Documento funcional pero desordenado, escaso o con capturas poco claras.
- **5 puntos** — Documento muy pobre, difícil de seguir o con capturas insuficientes.
- **0 puntos** — No existe documentación útil o la entrega carece completamente de sentido.