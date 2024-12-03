# SQL Server

#!/bin/bash

  

docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=<123Jhon@>" \

   -p 1433:1433 --name sql1 --hostname sql1 \

   -d \

   mcr.microsoft.com/mssql/server:2022-latest

  
  

# cambio de contreña

docker exec -it sql1 /opt/mssql-tools18/bin/sqlcmd \

-S localhost -U SA \

 -P "$(read -sp "Enter current SA password: "; echo "${REPLY}")" \

 -Q "ALTER LOGIN SA WITH PASSWORD=\"$(read -sp "Enter new SA password: "; echo "${REPLY}")\""

  
  

# logs

docker exec -t sql1 cat /var/opt/mssql/log/errorlog | grep connection

  

docker exec -it sql1 "bash"

  

sudo docker exec -it --user root sql1 "bash"


  
  conectdb /opt/mssql-tools/bin/sqlcmd -S db -U SA -P "1234@password"


/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "<123Jhon@>"

  


# create new database

docker exec -it sql1 /opt/mssql-tools/bin/sqlcmd \

   -S localhost -U SA -P "<123Jhon@>" \

   -Q "CREATE DATABASE TestDB"

  

# list all databases

docker exec -it sql1 /opt/mssql-tools/bin/sqlcmd \

   -S localhost -U SA -P "<123Jhon@>" \

   -Q "SELECT name FROM sys.databases"

  

docker stop sql1 && docker rm sql1

  
  

## installs driver

  

if ! [[ "16.04 18.04 20.04 22.04" == *"$(lsb_release -rs)"* ]];

then

    echo "Ubuntu $(lsb_release -rs) is not currently supported.";

    exit;

fi

  

curl https://packages.microsoft.com/keys/microsoft.asc | sudo tee /etc/apt/trusted.gpg.d/microsoft.asc

  

curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list

  

sudo apt-get update lsb-release

sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17

# optional: for bcp and sqlcmd

sudo ACCEPT_EULA=Y apt-get install -y mssql-tools

echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc

source ~/.bashrc

# optional: for unixODBC development headers

sudo apt-get install -y unixodbc-dev
