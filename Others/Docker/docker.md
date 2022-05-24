# Rquerimientos:

1. instalar docker Destokc [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
2. Intalar los plugins de vscode  
    1. [https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)
    2. [https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

# Docker simple Imagen

entre las funciones de docker es tener un servidor aparte del nuestro para ejecutar el proyecto, para ello creamos una build para con los archivos de nuestro proyecto que seran trasladados a el contenedor de docker ademas esta build debera tener algunas instalaciones para trabajar con las herramientas del proyecto

1. Creamos un archivo `Dokerfile` preferiblemente que este alado de manage.py
    
```py
FROM python:3.8-alpine3.15

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./requirements-deploy.txt ./

RUN  apk update \
  && apk add --no-cache gcc musl-dev postgresql-dev python3-dev  jpeg-dev zlib-dev \
  && pip install --upgrade pip

RUN python -m pip install -r requirements-deploy.txt 

COPY ./ ./

CMD [ "sh", "entrypoint.sh" ]
```

Details:
- `FROM python:3.8` ⇒ imagen que vamos a descargar desde docker hub, continene una terminal de linux expecializada para desarrollo con la herramienta objetiva
- `EXPOSE 8000` ⇒ le decimos que puerto usara dentro del container “localhost:8000”
- `ENV PYTHONDONTWRITEBYTECODE=1`
- `ENV PYTHONUNBUFFERED=1`

- Ejecucion de los comandos
```jsx
# Install pip requirements
#COPY backend/requirements.txt /backend/
#python -m pip install --upgrade pip
#RUN python -m pip install -r requirements.txt
#RUN python3 manage.py makemigrations
#RUN python3 manage.py migrate
```
        
> esta toda la logica que se va a ejecutar tras crear en contenedor, lo comento para que no se ejecute para acelerar el desarrollo en local, pero recuerda ejecutar estos comandos manualmente mas adelante
- `WORKDIR /app` ⇒ le decimos al contenedor que en “/app” sera el espacio de trabajo
- `COPY . ./app` ⇒ copia todos los archivos en “.” a la direccion dentro del contenedor “./app”
- `CMD ["gunicorn", "--bind", "0.0.0.0:8000", "pythonPath.to.wsgi"]`  ⇒ la ejecucion de gunicorn
2. Acontinuacion podemos ejecutar  la build lo cual llevar todo nuestro proyecto a un contenedor
    1. `docker build` ⇒ ejecuta la build con nuestro proyecto dentro del container
3. Cada ves que modifiquemos algo de nuestro proyecto tenemos que apagar la ejecucion del container y volver a crear la build y ejecutarla, evitaremos todo este proceso en el con el `devcontainer` mas adelante

#  Hoja de comandos para la administracion de docker:

`docker version` 

>“Docker hub para ver las imágenes disponibles”
`docker images`  ⇒ verifica todas las imagenes disponibles

`docker rmi [nombre de la imagen]`  ⇒ elimina una imagen del sistema

`docker rmi $(docker images -aq)` ⇒ Script que elimina todas las imagenes 

`docker pull hello-word` ⇒ descarga la imagen

`docker run hello-word` ⇒ ejecuta la imagen 

`docker search [nombre de la imagen]` ⇒ Busca las versiones de las imágenes

`docker run ubuntu echo 'hello world'`  ⇒ ejecuta los programas disponibles dentro de la imagen

`docker run -it ubuntu bash`  ⇒ ejecuta de manera interactiva los programas disponibles dentro de la imagen

“ todos los contenedores al crearse mueren vuelven a un estado en stop automáticamente”

`docker ps`  ⇒ muestra las imágenes que están en ejecución y sus datos

`docker ps -a`  ⇒ todos los contenedores existentes en stop

`docker ps -aq`  ⇒ todos los contenedores existentes en stop solo mostrando una lista de id’s

`docker rm [id o nombre]` ⇒  elimina del historial un contenedor ejecutado a través del nombre o id devuelto en el historial

`docker rm $(docker ps -aq)` ⇒ Script que elimina todos los contenedores en stop

`docker rm $(docker ps -aq) -f`  ⇒ Fuerza a detener y eliminar los contenedores

`docker start [id o nombre]` ⇒ vuelve a ejecutar un contenedor del historial o en stop

`docker stop [id o nombre]` ⇒ detiene el contenedor en ejcucion

`docker exec -it [id o nombre] bash`  ⇒ ejecuta un programa disponible dentro del contenedor en un contenedor previamente creado



