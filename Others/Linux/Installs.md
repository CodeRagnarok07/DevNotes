### python

```text
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.9.10
```

Metodo 2: archivos de python.org

```text
$ sudo apt update
$ sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
$ cd /tmp
$ wget https://www.python.org/ftp/python/3.9.10/Python-3.9.10.tgz
$ tar -xf Python-3.9.10.tgz
$ cd python-3.9.10
$ ./configure --enable-optimizations
$ sudo make altinstall
$ sudo make install
$ python3 --version
```

`$ sudo update-alternatives --config python3`  ⇒ version de python por default

```
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.4 1
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2
```

`$ sudo apt autoremove python3` ⇒ unistall python

## install pip
Option 1

```
$ sudo apt update
$ sudo apt install python3-venv python3-pip
```

Option 2

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py   ⇒ descarga paquetes iniciales
python get-pip.py
python -m pip install --upgrade pip
```


### Node.js

Instalación de Versiones: 

`sudo apt install wget`  instalador de versiones
`wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash`  
`source ~/.profile`  ⇒ permiso para ejecutar el wget
`nvm ls-remote`  ⇒ ver las versiones de node disponibles
`nvm install v16.15.1` `nvm install --lts`  ⇒ elegir versión

`sudo apt install nodejs`  instalacion de node
`sudo apt install npm` Instalacion de npm
`npm install -g npm@8.13.1`

$ sudo apt install yarn
To check the Installed version of Yarn:

$ yarn --version




[https://docs.microsoft.com/es-es/windows/dev-environment/javascript/nodejs-on-wsl](https://docs.microsoft.com/es-es/windows/dev-environment/javascript/nodejs-on-wsl)