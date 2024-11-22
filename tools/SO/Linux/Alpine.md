


### 1.- Add brew to alpine linux

```
apk update

git clone https://github.com/Homebrew/brew ~/.linuxbrew/Homebrew

mkdir ~/.linuxbrew/bin

ln -s ../Homebrew/bin/brew ~/.linuxbrew/bin

eval $(~/.linuxbrew/bin/brew shellenv)

brew --version

```

```
apk add curl git unzip neovim

apk add --no-cache build-base
```




### 2. Add Fish

```
apk add fish
```





### Dependecies


#### NVM

```
ARG PHP_VERSION=8.1

FROM php:${PHP_VERSION}-fpm-alpine AS coo-php
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
WORKDIR /srv/app

ENV NVM_DIR /usr/local/nvm # or ~/.nvm 

ENV NODE_VERSION 18

# Install nvm with node and npm
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.1/install.sh | bash; \
    && . ~/.nvm/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default
```