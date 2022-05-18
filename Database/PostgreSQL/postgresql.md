# Install postgres and create database

#### 1. **.- Install PostgresSQl**

```text
$ sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
$ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
$ sudo apt-get update
$ sudo apt-get -y install postgresql postgresql-contrib
$ sudo apt-get install libpq-dev
```

#### 2. **execute postgresql**

```text
$ sudo service postgresql status
$ sudo service postgresql start
```

#### 3. **Create database and password**

```text
sudo -u postgres psql => start console
postgres=# alter user Postgres with password 'newPasword';
postgres=# CREATE DATABASE name;
```


# pull heroku to local database

1. get DATABASE_URL
```text
heroku pg:psql 
Connecting to HEROKU_POSTGRESQL_RED...
```

2. pull to local db
```
PGUSER=localuserpg PGPASSWORD=localpassword heroku pg:pull DATABASE_URL mylocaldb --app nameherokuapp
```

   1. 1 solucion 1 crear otro usuario
    `$sudo -u postgres createuser -s $YOUR_USERNAME [-P]`
    `postgres=# ALTER USER postgres with password 'postgres';`


https://stackoverflow.com/questions/65222869/how-do-i-solve-this-problem-to-use-psql-psql-error-fatal-role-postgres-d