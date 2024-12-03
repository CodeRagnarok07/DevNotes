
# PRIMARY KEY y FOREIGN KEY

```SQL
CREATE TABLE tabla_1(
    id_tabla_1 INTEGER PRIMARY KEY AUTOINCREMENT
); 
CREATE TABLE tabla_2(
    id_tabla_2 INTEGER PRIMARY KEY AUTOINCREMENT,
    id_tabla_1 INTEGER,
    FOREING KEY (id_Tabla_1) REFERENCES tabla_1(idTabla_1)
    -- REFERENCES Hace referencia a la tabla 1
);
```

PRIMARY KEY: es la que provee a las tablas, siempre se agrega como id a todas las tablas ⇒  `INTEGER PRIMARY KEY AUTOINCREMENT`

#### Ejemplo1:

```SQL
CREATE TABLE carreras(
    idCarrera INTEGER 
    PRIMARY KEY AUTOINCREMENT,
    Nombre varchar(30), 
    duracion INTEGER
);

CREATE TABLE Alumnos(
    idAlumnos INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre varchar(30),
    apellido varchar(30),
    segundo_apellido varchar(30),
    email varchar(40),
    id_carrera INTEGER,
    FOREIGN KEY (id_carrera) REFERENCES carreras(idCarrera));
    -- FOREIGN KEY: Es la que accede a las llaves primarias ⇒ 
    -- FOREIGN KEY (id_carrera) REFERENCES carreras(idCarrera)



```