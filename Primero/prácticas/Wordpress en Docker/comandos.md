# Instalación y comprobación de Docker en Linux Mint

## 1. Comprobar si Docker ya está instalado

Antes de instalar nada, podemos comprobar si el comando `docker` ya está disponible en el sistema:

```bash
docker --version
```

Si Docker está instalado, aparecerá la versión.

Si no está instalado, aparecerá un mensaje indicando que el comando no existe o que no se ha encontrado.

---

## 2. Actualizar la lista de paquetes del sistema

Antes de instalar Docker, actualizamos la información de los repositorios:

```bash
sudo apt update
```

Este comando no actualiza todavía los programas instalados, sino que actualiza la lista de paquetes disponibles.

---

## 3. Actualizar el sistema

Después podemos actualizar los paquetes ya instalados:

```bash
sudo apt upgrade
```

Si nos pide confirmación, aceptamos con `s`.

---

## 4. Preparar el repositorio oficial de Docker

Docker CE no siempre viene directamente en los repositorios básicos de la distribución. Por eso vamos a añadir el repositorio oficial de Docker.

Primero instalamos algunos paquetes necesarios:

```bash
sudo apt install ca-certificates curl
```

Creamos la carpeta donde se guardarán las claves de los repositorios:

```bash
sudo install -m 0755 -d /etc/apt/keyrings
```

Descargamos la clave oficial de Docker:

```bash
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
```

Damos permisos de lectura a la clave:

```bash
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

Añadimos el repositorio oficial de Docker a `apt`:

```bash
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF
```

Actualizamos de nuevo la lista de paquetes:

```bash
sudo apt update
```

---

## 5. Comprobar qué versión de Docker tenemos disponible

Podemos comprobar qué versión de Docker tenemos instalada y cuál es la versión candidata disponible en los repositorios:

```bash
apt policy docker-ce
```

Debemos fijarnos en estas dos líneas:

```text
Installed: versión instalada
Candidate: versión disponible más reciente
```

Si `Installed` y `Candidate` son iguales, tenemos instalada la versión más reciente disponible.

Si `Installed` aparece como `(none)`, significa que Docker CE todavía no está instalado.

---

## 6. Instalar Docker CE

Instalamos Docker y sus componentes principales:

```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Aunque el paquete se llama `docker-ce`, el comando que usaremos después será simplemente:

```bash
docker
```

---

## 7. Comprobar que Docker se ha instalado correctamente

Comprobamos la versión de Docker:

```bash
docker --version
```

Comprobamos también Docker Compose:

```bash
docker compose version
```

---

## 8. Probar Docker con `hello-world`

Docker incluye una imagen de prueba llamada `hello-world`.

La ejecutamos con:

```bash
sudo docker run hello-world
```

Si todo funciona correctamente, Docker descargará la imagen, creará un contenedor, mostrará un mensaje de confirmación y terminará la ejecución.

Este ejemplo sirve para comprobar que Docker funciona, pero tiene una particularidad importante: el contenedor de `hello-world` no se queda ejecutándose. Se crea, muestra el mensaje y se detiene automáticamente.

Por eso, para practicar comandos como ver contenedores en ejecución, parar contenedores o acceder a un servicio desde el navegador, usaremos después un contenedor con `nginx`.

---

## 9. Evitar tener que usar `sudo` constantemente

Por defecto, en Linux puede ser necesario usar `sudo` para ejecutar comandos de Docker.

Para evitarlo, añadimos nuestro usuario al grupo `docker`:

```bash
sudo usermod -aG docker $USER
```

Después hay que cerrar sesión y volver a entrar.

También se puede reiniciar el sistema:

```bash
sudo reboot
```

Cuando volvamos a entrar, probamos Docker sin `sudo`:

```bash
docker run hello-world
```

Si funciona, ya podemos usar Docker sin escribir `sudo` en cada comando.

---

# Comandos básicos de Docker

Para practicar los comandos básicos vamos a usar `nginx`, un servidor web ligero.

A diferencia de `hello-world`, el contenedor de `nginx` sí se queda ejecutándose. Esto nos permitirá ver mejor qué contenedores están activos, cómo se detienen y cómo se eliminan.

---

## 1. Crear y ejecutar un contenedor con `nginx`

Ejecutamos:

```bash
docker run -d --name web-prueba -p 8080:80 nginx
```

Este comando crea y ejecuta un contenedor a partir de la imagen `nginx`.

Partes del comando:

```text
docker run           Crea y ejecuta un contenedor.
-d                   Ejecuta el contenedor en segundo plano.
--name web-prueba    Asigna el nombre web-prueba al contenedor.
-p 8080:80           Conecta el puerto 8080 del equipo con el puerto 80 del contenedor.
nginx                Imagen que se va a usar.
```

Si no tenemos descargada la imagen `nginx`, Docker la descargará automáticamente.

---

## 2. Comprobar que el contenedor está funcionando

Ejecutamos:

```bash
docker ps
```

Este comando muestra los contenedores que están en ejecución.

Debería aparecer un contenedor llamado:

```text
web-prueba
```

También podemos abrir el navegador y entrar en:

```text
http://localhost:8080
```

Si todo funciona correctamente, veremos la página de bienvenida de `nginx`.

---

## 3. Ver todos los contenedores

Para ver todos los contenedores, tanto los que están en ejecución como los que ya se han detenido, usamos:

```bash
docker ps -a
```

Diferencia importante:

```text
docker ps       Muestra solo contenedores en ejecución.
docker ps -a    Muestra todos los contenedores.
```

Aquí aparecerán tanto el contenedor de `nginx` como los contenedores que se hayan creado al ejecutar `hello-world`.

---

## 4. Ver las imágenes descargadas

Para ver las imágenes Docker descargadas en nuestro equipo, usamos:

```bash
docker images
```

Después de hacer las pruebas anteriores, deberían aparecer al menos estas imágenes:

```text
hello-world
nginx
```

Una imagen es como la plantilla a partir de la cual se crean los contenedores.

---

## 5. Parar el contenedor de `nginx`

Como `nginx` se queda ejecutándose, podemos detenerlo manualmente:

```bash
docker stop web-prueba
```

Después comprobamos de nuevo:

```bash
docker ps
```

El contenedor ya no debería aparecer entre los contenedores en ejecución.

Sin embargo, sigue existiendo como contenedor detenido. Para verlo:

```bash
docker ps -a
```

---

## 6. Volver a iniciar un contenedor detenido

Si el contenedor existe pero está detenido, podemos volver a iniciarlo:

```bash
docker start web-prueba
```

Comprobamos que vuelve a estar en ejecución:

```bash
docker ps
```

Y podemos volver a entrar en el navegador:

```text
http://localhost:8080
```

---

## 7. Reiniciar un contenedor

También podemos reiniciar un contenedor directamente:

```bash
docker restart web-prueba
```

Esto equivale a pararlo y volverlo a iniciar.

---

## 8. Eliminar un contenedor

Para eliminar un contenedor, primero debe estar detenido.

Lo paramos:

```bash
docker stop web-prueba
```

Después lo eliminamos:

```bash
docker rm web-prueba
```

Comprobamos que ya no aparece:

```bash
docker ps -a
```

---

## 9. Eliminar una imagen

Para eliminar una imagen descargada usamos:

```bash
docker rmi NOMBRE_DE_LA_IMAGEN
```

Por ejemplo, para eliminar la imagen de `hello-world`:

```bash
docker rmi hello-world
```

Para eliminar la imagen de `nginx`:

```bash
docker rmi nginx
```

Si Docker indica que la imagen está siendo usada por algún contenedor, primero habrá que eliminar el contenedor correspondiente.

Podemos comprobar los contenedores existentes con:

```bash
docker ps -a
```

---

# Resumen rápido

## Comprobaciones iniciales

```bash
docker --version
docker compose version
docker run hello-world
```

## Crear un contenedor de prueba con `nginx`

```bash
docker run -d --name web-prueba -p 8080:80 nginx
```

## Ver contenedores e imágenes

```bash
docker ps
docker ps -a
docker images
```

## Gestionar el contenedor

```bash
docker stop web-prueba
docker start web-prueba
docker restart web-prueba
docker rm web-prueba
```

## Eliminar imágenes

```bash
docker rmi hello-world
docker rmi nginx
```

## Crear un contenedor con WordPress usando Docker Compose

Una vez comprobado que Docker funciona correctamente, vamos a crear un entorno básico de WordPress.

En este caso no usaremos un único contenedor, porque WordPress necesita varios servicios para funcionar:

```text
WordPress       Aplicación web
Base de datos   MariaDB
```

Para gestionar varios contenedores relacionados usaremos `docker compose`.

---

## 1. Crear la carpeta del proyecto

Creamos una carpeta para guardar la configuración del entorno:

```bash
mkdir wordpress-docker
cd wordpress-docker
```

Dentro de esta carpeta guardaremos el archivo `compose.yaml` y algunas carpetas locales para conservar datos.

---

## 2. Crear la estructura de carpetas

Creamos una carpeta local para los archivos de WordPress que nos interesa conservar y modificar:

```bash
mkdir wp-content
```

La carpeta `wp-content` es importante porque ahí WordPress guarda elementos como:

```text
themes      Temas
plugins     Plugins
uploads     Archivos subidos desde WordPress
```

De esta forma, aunque borremos y volvamos a crear los contenedores, podremos conservar temas, plugins y archivos subidos.

La estructura inicial será:

```text
wordpress-docker/
└── wp-content/
```

---

## 3. Crear el archivo `compose.yaml`

Dentro de la carpeta `wordpress-docker`, creamos un archivo llamado:

```text
compose.yaml
```

El contenido del archivo será el siguiente:

```yaml
# En este archivo vamos a definir los contenedores necesarios
# para ejecutar WordPress con Docker Compose.

# Servicios que formarán parte de nuestra aplicación.
services:

  # Primer servicio: base de datos.
  # Lo llamamos "db" porque será la base de datos usada por WordPress.
  db:
    # Imagen que usará este contenedor.
    # En este caso usamos MariaDB, una base de datos compatible con MySQL.
    # lastest significa: 'descargate la última versión disponible'
    image: mariadb:latest

    # Nombre concreto que tendrá el contenedor.
    # Esto nos ayudará a identificarlo más fácilmente.
    container_name: wordpress-db

    # Si el contenedor se para por un error, o si reiniciamos el ordenador,
    # Docker intentará volver a levantarlo automáticamente, salvo que
    # lo hayamos parado manualmente.
    restart: unless-stopped

    # Variables de entorno.
    # Sirven para configurar MariaDB al crear el contenedor.
    environment:

      # Nombre de la base de datos que se creará para WordPress.
      MARIADB_DATABASE: wordpress

      # Usuario normal que usará WordPress para conectarse a la base de datos.
      MARIADB_USER: wordpress_user

      # Contraseña del usuario anterior.
      # En un entorno real debería ser una contraseña segura.
      MARIADB_PASSWORD: wordpress_password

      # Contraseña del usuario administrador de MariaDB.
      # En un entorno real también debería ser segura.
      MARIADB_ROOT_PASSWORD: root_password

    # Volúmenes del contenedor.
    # Los volúmenes permiten conservar datos aunque el contenedor se borre.
    volumes:
      # Guardamos los datos internos de MariaDB en un volumen llamado db_data.
      # /var/lib/mysql es la carpeta donde MariaDB guarda sus bases de datos.
      - db_data:/var/lib/mysql


  # Segundo servicio: WordPress.
  # Este será el contenedor que ejecuta la aplicación web.
  wordpress:

    # Última versión de la imagen oficial de WordPress.
    image: wordpress:latest

    # Nombre concreto que tendrá el contenedor.
    container_name: wordpress-web

    restart: unless-stopped

    # Indica que WordPress depende de la base de datos.
    # Docker Compose iniciará primero el servicio "db".
    depends_on:
      - db

    # Puertos.
    # Permiten acceder desde nuestro ordenador al servicio web del contenedor.
    ports:

      # Puerto externo(host):puerto interno(contendor)
      # 8080 es el puerto que usaremos en nuestro ordenador.
      # 80 es el puerto web dentro del contenedor.
      - "8080:80"

    # Variables de entorno para configurar WordPress.
    environment:

      # Servidor de base de datos.
      # Usamos "db" porque ese es el nombre del servicio de MariaDB.
      WORDPRESS_DB_HOST: db

      # Nombre de la base de datos.
      # Debe coincidir con MARIADB_DATABASE.
      WORDPRESS_DB_NAME: wordpress

      # Usuario de la base de datos.
      # Debe coincidir con MARIADB_USER.
      WORDPRESS_DB_USER: wordpress_user

      # Contraseña de la base de datos.
      # Debe coincidir con MARIADB_PASSWORD.
      WORDPRESS_DB_PASSWORD: wordpress_password

    # Volúmenes de WordPress.
    volumes:

      # Conectamos la carpeta local ./wp-content
      # con la carpeta interna de WordPress /var/www/html/wp-content.
      #
      # Esto nos permite conservar y modificar temas, plugins y archivos subidos
      # desde fuera del contenedor.
      - ./wp-content:/var/www/html/wp-content


# Sección de volúmenes del contenedor.
# En la sección final volumes solo se declaran los volúmenes gestionados por Docker, como db_data. Las carpetas locales enlazadas directamente desde el proyecto, como ./wp-content, no se declaran ahí porque ya se indican con su ruta dentro del propio servicio.
volumes:
  # Volumen donde se guardará la base de datos de MariaDB.
  db_data:
```

---

## 4. Explicación del archivo `compose.yaml`

El archivo define dos servicios:

```text
db          Base de datos MariaDB
wordpress   Aplicación WordPress
```

El servicio `db` usa la imagen:

```yaml
image: mariadb:11
```

Esta imagen crea un contenedor con MariaDB, que será la base de datos usada por WordPress.

El servicio `wordpress` usa la imagen:

```yaml
image: wordpress:latest
```

Esta imagen contiene WordPress junto con el entorno necesario para ejecutarlo.

---

## 5. Puertos

En la parte de WordPress aparece:

```yaml
ports:
  - "8080:80"
```

Esto significa:

```text
8080    Puerto de nuestro ordenador
80      Puerto interno del contenedor
```

Por eso accederemos a WordPress desde el navegador usando:

```text
http://localhost:8080
```

---

## 6. Variables de entorno

Las variables de entorno sirven para pasar configuración a los contenedores.

En la base de datos tenemos:

```yaml
MARIADB_DATABASE: wordpress
MARIADB_USER: wordpress_user
MARIADB_PASSWORD: wordpress_password
MARIADB_ROOT_PASSWORD: root_password
```

Con esto se crea una base de datos llamada `wordpress` y un usuario llamado `wordpress_user`.

En WordPress tenemos:

```yaml
WORDPRESS_DB_HOST: db
WORDPRESS_DB_NAME: wordpress
WORDPRESS_DB_USER: wordpress_user
WORDPRESS_DB_PASSWORD: wordpress_password
```

Estos datos permiten que WordPress se conecte al contenedor de la base de datos.

El valor importante es:

```yaml
WORDPRESS_DB_HOST: db
```

`db` es el nombre del servicio de la base de datos dentro de Docker Compose. Docker permite que los contenedores del mismo proyecto se comuniquen entre sí usando el nombre del servicio.

---

## 7. Volúmenes

En la base de datos aparece:

```yaml
volumes:
  - db_data:/var/lib/mysql
```

Esto guarda los datos de MariaDB en un volumen llamado `db_data`.

Gracias a esto, si paramos o recreamos el contenedor, la base de datos no se pierde automáticamente.

En WordPress aparece:

```yaml
volumes:
  - ./wp-content:/var/www/html/wp-content
```

Esto conecta la carpeta local `wp-content` con la carpeta interna de WordPress.

Es decir:

```text
./wp-content                  Carpeta en nuestro ordenador
/var/www/html/wp-content      Carpeta dentro del contenedor
```

Esto nos permitirá conservar y modificar temas, plugins y archivos subidos.

---

## 8. Levantar WordPress

Desde la carpeta donde está el archivo `compose.yaml`, ejecutamos:

```bash
docker compose up -d
```

La opción `-d` significa que los contenedores se ejecutarán en segundo plano.

Docker descargará las imágenes necesarias y creará los contenedores.

---

## 9. Comprobar que los contenedores están funcionando

Ejecutamos:

```bash
docker ps
```

Deberían aparecer dos contenedores:

```text
wordpress-web
wordpress-db
```

También podemos usar:

```bash
docker compose ps
```

Este comando muestra los contenedores del proyecto actual de Docker Compose.

---

## 10. Abrir WordPress en el navegador

Abrimos el navegador y entramos en:

```text
http://localhost:8080
```

Si todo funciona correctamente, aparecerá la pantalla inicial de instalación de WordPress.

Ahí podremos elegir idioma, crear el usuario administrador y completar la instalación.

---

## 11. Instalar plugins o temas

Una vez dentro del panel de administración de WordPress, podemos instalar plugins y temas desde la propia interfaz.

Por ejemplo:

```text
Plugins → Añadir nuevo
Apariencia → Temas
```

Como hemos enlazado la carpeta `wp-content`, los plugins y temas quedarán guardados en la carpeta local:

```text
wordpress-docker/wp-content/
```

Por ejemplo, después de instalar plugins o temas, la estructura puede quedar así:

```text
wordpress-docker/
├── compose.yaml
└── wp-content/
    ├── plugins/
    ├── themes/
    └── uploads/
```

---

## 12. Parar WordPress

Para parar los contenedores sin borrarlos:

```bash
docker compose stop
```

Para volver a iniciarlos:

```bash
docker compose start
```

---

## 13. Parar y eliminar los contenedores

Para parar y eliminar los contenedores del proyecto:

```bash
docker compose down
```

Esto elimina los contenedores, pero no elimina automáticamente el volumen de la base de datos.

Por tanto, los datos de WordPress deberían conservarse.

---

## 14. Borrar también la base de datos

Si queremos borrar completamente el entorno, incluyendo la base de datos, usamos:

```bash
docker compose down -v
```

La opción `-v` elimina también los volúmenes.

Cuidado: esto borra la base de datos de WordPress.

---

## 15. Ver los logs

Si algo falla, podemos ver los mensajes de los contenedores con:

```bash
docker compose logs
```

Para ver los logs en tiempo real:

```bash
docker compose logs -f
```

También podemos ver los logs de un servicio concreto:

```bash
docker compose logs wordpress
```

O de la base de datos:

```bash
docker compose logs db
```

---

## 16. Reiniciar el entorno

Para reiniciar los contenedores:

```bash
docker compose restart
```

También podemos reiniciar solo WordPress:

```bash
docker compose restart wordpress
```

O solo la base de datos:

```bash
docker compose restart db
```

---

## 17. Entrar en el contenedor de WordPress

Podemos abrir una terminal dentro del contenedor de WordPress:

```bash
docker exec -it wordpress-web bash
```

Esto puede ser útil para inspeccionar archivos dentro del contenedor.

Para salir:

```bash
exit
```

---

## 18. Resumen rápido

Crear y arrancar WordPress:

```bash
mkdir wordpress-docker
cd wordpress-docker
mkdir wp-content
docker compose up -d
```

Comprobar contenedores:

```bash
docker ps
docker compose ps
```

Abrir WordPress:

```text
http://localhost:8080
```

Parar WordPress:

```bash
docker compose stop
```

Volver a iniciarlo:

```bash
docker compose start
```

Eliminar contenedores:

```bash
docker compose down
```

Eliminar contenedores y base de datos:

```bash
docker compose down -v
```

Ver logs:

```bash
docker compose logs
docker compose logs -f
```

---

## Idea clave

Con `docker run` podemos crear contenedores individuales, como hicimos con `nginx`.

Con `docker compose` podemos definir una aplicación formada por varios contenedores relacionados.

WordPress necesita al menos dos partes:

```text
WordPress
Base de datos
```

Por eso `docker compose` es una forma más cómoda y ordenada de levantar este tipo de entorno.

