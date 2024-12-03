-- VALIDACIONS
(

    -- PRIMARY KEY

    table_id SERIAL,    -- auto incremental [ postgresql, mysql]
    PRIMARY KEY (table_id) -- obligatorio definir la clave primaria

    table_id SERIAL PRIMARY KEY,     -- segunda manera de definir primary key

    -- FOREIGN KEY
	oter_table_id FOREIGN KEY REFERENCES other_table(oter_table_id),-- DEFINE ESTE CAMPO COMO LLAVE FORANEA
    client_id INT REFERENCES clients(clients_id)

    FOREIGN KEY (oter_table_id) REFERENCES other_table(oter_table_id),-- DEFINE ESTE CAMPO COMO LLAVE FORANEA

    -- NOT NULL => no en blanco

    edad INT,   -- campo normal int
	name1 VARCHAR(100) NOT NULL, -- texto longitud(100) no ocupable
	name2 CHAR(100) NOT NULL, -- texto longitud() ocupable con espacios en blanco

    descripcion TEXT,               -- texto plano puede decidirse la longitud
	init_date DATE DEFAULT CURRENT_DATE -- DEFAULT NOW(), -- fecha actual defualt automatica

    -- CHECK => define una condicion
    product_stock INT CHECK(product_stock > 0 ) DEFAULT 0,

  

);
