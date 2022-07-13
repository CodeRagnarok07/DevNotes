[doc](https://yarnpkg.com/getting-started/install)




#  solucion

 had the same issue on Ubuntu 17.04.

This solution worked for me:

sudo apt remove cmdtest
sudo apt remove yarn
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt-get update
sudo apt-get install yarn -y
then

yarn install
result:

yarn install v1.3.2
warning You are using Node "6.0.0" which is not supported and may encounter bugs or unexpected behaviour. Yarn supports the following server range: "^4.8.0 || ^5.7.0 || ^6.2.2 || >=8.0.0"
info No lockfile found.
[1/4] Resolving packages...
[2/4] Fetching packages...
[3/4] Linking dependencies...
[4/4] Building fresh packages...

info Lockfile not saved, no dependencies.
Done in 0.20s.


yarn add gsap reveal.js

yarn add express mongoose



# Usage
```py
# Accessing the list of commands
$ yarn help

# Starting a new project
$ yarn init

# Installing all the dependencies
$ yarn
$ yarn install

# Adding a dependency
yarn add [package]
yarn add [package]@[version]
yarn add [package]@[tag]

# Adding a dependency to different categories of dependencies
yarn add [package] --dev  # dev dependencies
yarn add [package] --peer # peer dependencies

# Upgrading a dependency
yarn up [package]
yarn up [package]@[version]
yarn up [package]@[tag]

# Removing a dependency
yarn remove [package]

# Upgrading Yarn itself
yarn set version latest
yarn set version from sources
```