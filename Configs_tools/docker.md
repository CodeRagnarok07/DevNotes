

## delete all images and containers

docker rm -vf $(docker ps -aq) && docker rmi -f $(docker images -aq)


## docker compose

docker compose up -d --force-recreate



### ejecucion interactiva

1.- crea el contenedor 
```sh
docker run <imagen name>
```
2.- docker start <id>
3.- docker exec -it 789 sh




### ejecucion iteractiva de archlinux

docker run -d --tty --name testarch archlinux



## Images
docker images

docker search <imagen name>

## ejecutar

docker run <imagen name>
docker run -it <imagen> | ejecuta de manera interactiva

## administracion de contenedores
docker ps           | contenedores en ejecucion
docker ps -a        | historia de contenedores ejecutados 
docker ps -aq       | listado de id del historial

------
docker rm <id-contenedor>   | elimina contendor
docker start <id-contenedor> | inicia contendor apagado del historial
docker stop

-f | forzar la ejecucion del comando (eliminar)

--------
docker exec -it <id> <comand> | volver a entrar en un contenedor en ejecucion 
ej: [ docker exec -it mydistro sh ]

###  combinar comando con bash
docker stop $(docker ps -aq) | detiene todos los contenedores
docker rm $(docker ps -aq)


#### parametros de docker run
docker run <- parametros - - > <imagen> <comando>

-p 3000:80      | administra el puerto local:contenedor 
-d              | ejecuta en segundo plano el conenedor sin bloquear la terminal
--name          | agrega un nombre al contenedor




