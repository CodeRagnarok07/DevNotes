### Add user with sudo



agregar nuevo usuario
```
apt-get update && apt upgrade
apt install sudo 

sudo su
useradd|adduser $new_user
passwd $new_user
usermod -aG sudo $new_user
mkdir /home/$new_user

exit
su - $new_user

sudo whoami

sudo chown -R $USER:$USER /home/$USER




```

### agrgar usuario por defecto
```sh
sudo nano /etc/wsl.conf
```

`/etc/wsl.conf`
```
[user]
default=tu_usuario
```

```bash
exit
wsl --shutdown
```


## useradd
```
apt install sudo -y
useradd -rm -d /home/rag -s /bin/bash -g root -G sudo -u 998 rag
su rag
sudo chown -R $USER:$USER /home/$USER

USER ubunt
```

`useradd` options (see: `man useradd`):
- `-r`, `--system` Create a system account. see: [Implications creating _system accounts_](https://unix.stackexchange.com/q/213101/21471)
- `-m`, `--create-home` Create the user's home directory.
- `-d`, `--home-dir HOME_DIR` Home directory of the new account.
- `-s`, `--shell SHELL` Login shell of the new account.
- `-g`, `--gid GROUP` Name or ID of the primary group.
- `-G`, `--groups GROUPS` List of supplementary groups.
- `-u`, `--uid UID` Specify user ID. see: [Understanding how uid and gid work in Docker containers](https://medium.com/@mccode/understanding-how-uid-and-gid-work-in-docker-containers-c37a01d01cf)
- `-p`, `--password PASSWORD` Encrypted password of the new account (e.g. `ubuntu`).
