# Docker compose

podemos ejecutar nuestro proyecto normalmente dentro del container, el problema es que nuestro container no tiene una lectura para nuestra base de datos local, también hay otros servicios locales que necesita nuestro proyecto para ejecutarse, por ello usamos el compose

1. Creamos un archivo docker-compose.yml
2. agregamos esta configuracion
    
```
version: '3.4'

services:
  # redis:
  #   restart: always
  #   image: redis:5
  #   ports:
  #     - "6379:6379"

  db:
    restart: always
    #restart: unless-stopped
    image: postgres:14.1-alpine3.15 
    volumes:
      - ./data/db:/var/lib/postgresql/data
    ports:
      - 5431:5432 # para que sea visible en nuestro entorno local 
    environment:
      - POSTGRES_NAME=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres

  django:    
    restart: always
    container_name: django
    build:      
      context: .
      dockerfile: ./local.Dockerfile
    command: >
      sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
    ports:
      - "8000:8000"
    environment:
      - POSTGRES_NAME=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_HOST=db
      - ALLOWED_HOSTS=127.0.0.1, localhost     
      - DJANGO_KEY=123
      - DEBUG=True

    volumes:
      - .:/app
    depends_on:
      - db
```

>Explicaciones:
cada subcategoria de redis sera una imagen o una terminal de linux que se ejecutara en nuestro container,  ose la maquina virtual que creamos
    
```python
django:    # => nombre de imgen personalizada
restart: always # => momento de ejecuciones 
image: django  # => nombre de imgen personalizada
container_name: django  # nombre de imgen personalizada
build:      # => definimos que imagen tendra esta terminal
  context: .  # => definimos en que ruta buscar la imagen
  dockerfile: ./Dockerfile # => el archivo que creamos en el paso anteriro
# Overrides default command so things don't shut down after the process ends.
command: sleep infinity   
# command: python manage.py runserver 0.0.0.0:8000
ports:
  - "8000:8000" #=> el puerto que usa la imagen : el puerto en el que estara disponible en el enrtonro local
environment: #=> variables de entorno en el path
  - POSTGRES_NAME=postgres
  - POSTGRES_USER=postgres
  - POSTGRES_PASSWORD=postgres
  - ALLOWED_HOSTS=127.0.0.1, localhost     

volumes:
  - .:/workspace #=> define que archivos de nuestro projecto se llevara al container
depends_on: #=> definecon que otras terminales se va a conocetar
  - db
```
    
3. aquí prefiero agregar las variables de entorno a nuestro proyecto local para poder alternar entre entornos virtuales
    1. definición de los datos de postgres
    2. sttigns usando las nuevas variables de entorno
    3. variables de entorno definidas en el docker-compose
4. ejecutamos `docker-compose build` en la terminal deberia funcionar correctamente
5. Recuerda ejecutar los comandos omitidos en el Dockerfile

