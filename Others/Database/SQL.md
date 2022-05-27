### PRIMARY KEY y FOREIGN KEY

`CREATE TABLE tabla_1(idTabla_1 INTEGER PRIMARY KEY AUTOINCREMENT);` 

`CREATE TABLE tabla_2(idTabla_2 INTEGER PRIMARY KEY AUTOINCREMENT, id_Tabla_1 INTEGER,FOREING KEY (id_Tabla_1) REFERENCES tabla_1(idTabla_1));` (Hace referencia a la tabla 1)

PRIMARY KEY: es la que provee a las tablas, siempre se agrega como id a todas las tablas ⇒  `INTEGER PRIMARY KEY AUTOINCREMENT`

Ejemplo:

`CREATE TABLE carreras(idCarrera INTEGER PRIMARY KEY AUTOINCREMENT,Nombre varchar(30), duracion INTEGER);`

FOREIGN KEY: Es la que accede a las llaves primarias ⇒ `FOREIGN KEY (id_carrera) REFERENCES carreras(idCarrera)`

Ejemplo

`CREATE TABLE Alumnos(idAlumnos INTEGER PRIMARY KEY AUTOINCREMENT, nombre varchar(30), apellido varchar(30), segundo_apellido varchar(30), email varchar(40), id_carrera INTEGER, FOREIGN KEY (id_carrera) REFERENCES carreras(idCarrera));`

### METODOS QUERY

INSERT:

`INSERT INTO tabla (campo1, campo2) VALUES('campo 1', 'campo2')`

SELECT

`SELECT * FROM tablaName` where campo2 = ‘todos los que tengan este nombre’

trae todo de la tabla

UPDATE

`UPDATE tablaName SET campo1='alquimista', campo2='30 min' WHERE idTabla=4`

trae todo de la tabla

DELETE

`DELETE FROM nameTable WHERE idTabla=3`

trae todo de la tabla

### CLAUSULAS WHERE

la clausular WhERE se puede usar en SELECT UPDATE DELETE 

 `SELECT * FROM Table WhERE campo1 = 'dato1'`

- Operadores Logicos de WHERE
    
    `SELECT * FROM Table WhERE NOT campo1 = 'dato1'`
    
    AND ; selecionar dos elementos
    
    OR ;  cumple una o la otra por igual las dos
    
    NOT;  Negacion (Es el unico que se coloca adelante de la condicion)
    
    Combinaciones
    
    `SELECT * FROM Table WhERE idTable=2 AND campo1 = 'dato1' OR idCapmpo > 1`
    

- Operadores relacionales de WHERE
    
    `SELECT * FROM Table WhERE campo1 <> 'dato1'`
    
    = ; Igual
    
    <> ; Distinto
    
    > ; Mayor que
    
     < ; Menor que
    
     >= ; mayor o igual
    
     <= ; Menor o igual
    
- BETWEEN
    
    `SELECT * FROM carreras WHERE duracion >=2 AND duracion <=3`
    
    `SELECT * FROM carreras WHERE duracion BETWEEN 1 AND 3`
    
    `SELECT * FROM carreras WHERE duracion BETWEEN 1 AND 3`
    

- IN: recupera varios como AND
    
    `SELECT * FROM carreras WHERE duracion IN (1, 2 , 3)`
    

- LIKE; información parcial
    
    `SELECT * FROM carreras WHERE nombre LIKE 'a%’`
    
    NOT = `SELECT * FROM carreras WHERE nombre NOT LIKE 'a%’`
    
    OPERADORES DE LIKE
    
    `a%` ; comienza con
    
    `_a%` ; comodin por que no se conocen las primeras letra pero si la segunda
    
    `%a` ; Termina con 
    
    `%a%` ; no empieza con a ni termina, pero lo tienen en el centro
    
    `a%` ; comienza con
    
    `a%` ; comienza con
    

## funciones de agrupamiento ( solo numéricos)

- COUNT ; recupera la cantidad de resultados
    - `SELECT count(idCarrera) FROM carreras WHERE duracion = 2`
- SUM; total de la id de los resultados
    - `SELECT sum(idCarrera) FROM carreras WHERE duracion = 2`
- MAX; el máximo encontrado de entre todos los resultados
    - `SELECT max(duracion) FROM carreras`
- MIN
    - `SELECT min(duracion) FROM carreras`
- AVG
    - `SELECT AVG(duracion) FROM carreras`

### OTROS OPERADORES

ORDER by ; ordenar `SELECT * FROM carreras ORDER by duracion`