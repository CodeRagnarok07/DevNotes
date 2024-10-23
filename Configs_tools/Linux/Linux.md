

### Linea de comandos


- contenido de directorio
	- `ls -als`
	- -a => ocultos
	- l => lista
	- s => datos humanos
- Copias
	- cp -a => copia las carpetas de forma recursiva
- Borrar => `rm -rf directorio`
	- r => recursivo
	- f => force
- Mover o renombrar => `mv file  newrute`
- Copiar muchos archivos sincronizados sin repetir los existentes de la copia
	- `rsync -av` => copia los elemntos de una carpeta a otra
- `du -sh /directorio`
	- Muestra el peso del directorio en humano (h) 

informacion de archivos
- `stat nombre-del-archivo` 


 Busqueda de archivos 
 - por nombre => `sudo find /dir -iname 'fish.config'`
	 - i => no case sensitive



- cositas
	- `cal ` => muestra un calendario
	- `date ` => muestra la fecha actual
	- `bc` => calculadora simple


- curl 
	- Hace peticiones http
	- `curl ifconfig.me` => muestra la ip del servidor

- grep
	- Filtra la salida de un comando por el parametro de el primer argument
	- `grep hola ./file.txt`  => solo muestra las lineas que contienen  hola
	- `curl pagina.com | grep video` => filtra la salida del primer comando
	- parametros
		- -v filtra negando el parametro
		- -r Recusivo => carpeta 
		- -l solo muestra el archivo que fue filtrado mejor con 


Ver historial
- `history` =>muestra todo el historial
- `history | grep comando` => para filtar o buscar
- `C-r` => modo interativo busca el anterior repitiendo el shortcut
