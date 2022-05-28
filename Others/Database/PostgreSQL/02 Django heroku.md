# pull heroku to local database

### 1. get DATABASE_URL
```text
heroku pg:psql 
Connecting to HEROKU_POSTGRESQL_RED...
```

### 2. pull to local db
```
PGUSER=localuserpg PGPASSWORD=localpassword heroku pg:pull DATABASE_URL mylocaldb --app nameherokuapp
```
1 solucion 1 crear otro usuario
`$sudo -u postgres createuser -s $YOUR_USERNAME [-P]`
`postgres=# ALTER USER postgres with password 'postgres';`

https://stackoverflow.com/questions/65222869/how-do-i-solve-this-problem-to-use-psql-psql-error-fatal-role-postgres-d
```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'test', #< == nombre de la base de datos creada en pgadmin
            'USER': 'postgres',
            'PASSWORD': 'clave de instalacion',
            'HOST': 'localhost',
            'PORT': 5432,
        }
    }
```

