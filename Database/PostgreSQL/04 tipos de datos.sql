
-- VALIDACIONS
(
    NOT NULL, 
    fecha DATE DEFAULT CURRENT_DATE, -- fecha actual defualt
    user_id INT,   -- campo normal int
	FOREIGN KEY REFERENCES user_table(user_id)-- DEFINE ESTE CAMPO COMO LLAVE FORANEA
)


CREATE TABLE user_table(
    user_id SERIAL,    -- auto incremental [ postgresql, mysql]
    PRIMARY KEY (user_id) -- obligatorio definir la clave primaria
);

CREATE TABLE task(
	task_name VARCHAR(100) NOT NULL, -- texto longitud(22)
    description TEXT,               -- texto plano puede decidirse la longitud
	date DATE DEFAULT CURRENT_DATE, -- fecha actaula automatica
    task_id SERIAL PRIMARY KEY,     -- segunda manera de definir llave foranea
    

    -- llave foranea
	user_id INT,         -- campo normal int seranado llave foranea
	FOREIGN KEY (user_id) REFERENCES user_table(user_id)-- DEFINE ESTE CAMPO COMO LLAVE FORANEA
	
);



SELECT * FROM user_table;

