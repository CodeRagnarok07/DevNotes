### Run mssql in docker

[[Dev/DevOps/database/SQL Server]]

## Set django proyect

dependencies
```
pip install django mssql-django django-environ dj-database-url
```


`settings.py`
```python
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': env("DATABASE_NAME"),
        'USER': env("DATABASE_USER"),
        'PASSWORD': env("DATABASE_PASSWORD"),
        'HOST': env("DATABASE_HOST"),
        'PORT': env("DATABASE_PORT"),
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}
```
or
```python
DATABASES['default'] = dj_database_url.config(default=os.getenv('DATABASE_URI', 'sqlite:///db.sqlite3'))
if DATABASES['default']['ENGINE'] == 'sql_server.pyodbc':
    DATABASES['default']['OPTIONS'] = {'driver': 'ODBC Driver 17 for SQL Server'}
```


### Dependencies need to install msodbcsql17 mssql-tools

 (Debian 11)
```sh
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list
```
(for ubuntu 20.04) 
```sh
curl https://packages.microsoft.com/keys/microsoft.asc | sudo tee /etc/apt/trusted.gpg.d/microsoft.asc
curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list
```

Install
```bash
apt-get update
RUN ACCEPT_EULA=Y apt-get install msodbcsql17 mssql-tools -y
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
source ~/.bashrc
```


Check conections with mssql-tools
```
/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "1234@password"
```



```
python manage.py migrate --fake-initial
```