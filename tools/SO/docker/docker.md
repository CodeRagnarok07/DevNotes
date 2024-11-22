
###  Docker install

```sh
curl -fsSL https://get.docker.com -o- get-docker.sh | bash
```
Add docker to sudo
```sh
# sudo groupadd docker 
sudo usermod -aG docker $USER
newgrp docker
```
Check installer
```sh
docker --version
docker compose version
```






### Scripts y Comandos de Docker

Borra todas las images
```sh
docker rm -vf $(docker ps -aq) && docker rmi -f $(docker images -aq)
```

ejecucion iteractiva de archlinux

```
docker run -d --tty --name testarch archlinux
```



### Orden de ejecucion

1. descarga  la imagen `docker pull <imagen name>`
2. crea el contenedor `docker pull <imagen name>`
3. levanta el conenedor `docker start <id></id></id> `
4. ejecuta algun comando ` docker exec -it 789 sh`


# tags de contenedor

#### Docker run
Para docker run
`docker run <- parametros - - > <imagen> <comando>`

| Tag            | Descripcion                                                    |
| -------------- | -------------------------------------------------------------- |
| `-t`, `--name` | nombre del contendor para ser llamado                          |
| `-e`           | variable de entorno                                            |
|                |                                                                |
| -p 3000:80     | administra el puerto local:contenedor                          |
| -d             | ejecuta en segundo plano el conenedor sin bloquear la terminal |
| --name         | agrega un nombre al contenedor                                 |


example
```
docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=<1234@pass>" \
   -p 1433:1433 --name sql1 --hostname sql1 \
   -d \
   mcr.microsoft.com/mssql/server:2022-latest
```
 


## Images

| `docker images` | Lista las imagenes se puede usar los filtros |
| `docker search <imagen name>` | busqueda de imagen |

#### administración de contenedores
 
| comando                        | description                                 |
| ------------------------------ | ------------------------------------------- |
| docker ps                      | contenedores en ejecucion                   |
| docker ps -a                   | historia de contenedores ejecutados         |
| docker ps -aq                  | listado de id del historial                 |
| `docker stop <id-contendor>`   | elimina contendor                           |
| `docker start <id-contenedor>` | inicia contendor apagado del historial <br> |
| `docker rm <id-contenedor>`    | elimina contendor                           |
| -f                             | forzar la ejecucion del comando (eliminar)  |
















