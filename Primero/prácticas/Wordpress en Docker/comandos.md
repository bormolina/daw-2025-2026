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

