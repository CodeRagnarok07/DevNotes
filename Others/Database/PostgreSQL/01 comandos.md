### Uso de la base de datos

- `psql --version`  ⇒ Chequear la version
- `sudo -u postgres psql`
    - postgres ⇒ usuario predeterminado
    - psql ⇒ comando de iniciación de la base de datos

Comenzar la base de datos

- `sudo service postgresql status` for checking the status of your database.
- `sudo service postgresql start` to start running your database.
- `sudo service postgresql stop` to stop running your database.
- `sudo passwd postgres` You will get a prompt to enter your new password.


### Comandos de postgreSql terminal

- `\l`  ⇒ listado de bases de datos
- `\q`  ⇒ salir de psql
- `\c` ⇒ entra en la base de datos listada
- `alter user postgres with password 'newPasword';`  ⇒ modifica o restablece la contraseña del usuario `postgres`
- Una ves dentro de una base de datos con `\c` se hace uso de las sentencias sql
- `drop database;`  ⇒ elimina la base de datos

- hotkey
    - `q` ⇒ salir

`CREATE DATABASE name;`  ⇒ crea una nueva base de datos

***Comandos de ayuda***

En consola los dos principales comandos con los que podemos revisar el todos los comandos y consultas son:

- **`\?`** Con el cual podemos ver la lista de todos los comandos disponibles en consola, comandos que empiezan con backslash ( \ )

![https://static.platzi.com/media/user_upload/2-f3fd936e-bdb2-4583-afce-1899ca222a77.jpg](https://static.platzi.com/media/user_upload/2-f3fd936e-bdb2-4583-afce-1899ca222a77.jpg)

- **`\h`** Con este comando veremos la información de todas las consultas SQL disponibles en consola. Sirve también para buscar ayuda sobre una consulta específica, para buscar información sobre una consulta específica basta con escribir **`\h`** seguido del inicio de la consulta de la que se requiera ayuda, así: **`\h ALTER`**

De esta forma podemos ver toda la ayuda con respecto a la consulta ***ALTER***

![https://static.platzi.com/media/user_upload/3-ee850ea6-271e-4826-9d8f-aa054dddc3fc.jpg](https://static.platzi.com/media/user_upload/3-ee850ea6-271e-4826-9d8f-aa054dddc3fc.jpg)

***Comandos de navegación y consulta de información***

- **`\c`** Saltar entre bases de datos
- **`\l`** Listar base de datos disponibles
- **`\dt`** Listar las tablas de la base de datos
- **`\d <nombre_tabla>`** Describir una tabla
- **`\dn`** Listar los esquemas de la base de datos actual
- **`\df`** Listar las funciones disponibles de la base de datos actual
- **`\dv`** Listar las vistas de la base de datos actual
- **`\du`** Listar los usuarios y sus roles de la base de datos actual

***Comandos de inspección y ejecución***

- **`\g`** Volver a ejecutar el comando ejecutando justo antes
- **`\s`** Ver el historial de comandos ejecutados
- **`\s <nombre_archivo>`** Si se quiere guardar la lista de comandos ejecutados en un archivo de texto plano
- **`\i <nombre_archivo>`** Ejecutar los comandos desde un archivo
- **`\e`** Permite abrir un editor de texto plano, escribir comandos y ejecutar en lote. **\e** abre el editor de texto, escribir allí todos los comandos, luego guardar los cambios y cerrar, al cerrar se ejecutarán todos los comandos guardados.
- **`\ef`** Equivalente al comando anterior pero permite editar también funciones en PostgreSQL

***Comandos para debug y optimización***

- **`\timing`** Activar / Desactivar el contador de tiempo por consulta

***Comandos para cerrar la consola***

- **`\q`** Cerrar la consola


```
\? => lista de todos los comandos disponibles en consola
\h => Lista de toda la ayuda disponible \h ALTER

\c => Saltar entre bases de datos

\l => Listar base de datos disponibles

\dt => Listar las tablas de la base de datos

\d => <nombre_tabla> Describir una tabla

\dn => Listar los esquemas de la base de datos actual

\df => Listar las funciones disponibles de la base de datos actual

\dv => Listar las vistas de la base de datos actual

\du => Listar los usuarios y sus roles de la base de datos actual

Comandos de inspección y ejecución

\g => Volver a ejecutar el comando ejecutando justo antes

\s => Ver el historial de comandos ejecutados

\s => <nombre_archivo> Si se quiere guardar la lista de comandos ejecutados en un archivo de texto plano

\i => <nombre_archivo> Ejecutar los comandos desde un archivo

\e => Permite abrir un editor de texto plano, escribir comandos y ejecutar en lote. \e abre el editor de texto, escribir allí todos los comandos, luego guardar los cambios y cerrar, al cerrar se ejecutarán todos los comandos guardados.

\ef => Equivalente al comando anterior pero permite editar también funciones en PostgreSQL

Comandos para debug y optimización

\timing Activar / Desactivar => el contador de tiempo por consulta

\q => Cerrar la consola
```


 public | django_migrations             | table | angel
 public | django_session                | table | angel
 public | wordbook_flashcard            | table | angel
 public | wordbook_wordterm             | table | angel