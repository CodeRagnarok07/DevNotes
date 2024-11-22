


## Instalar Yay - AUR

sudo pacman -S --needed base-devel git
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si


## users change

useradd -m test "add ne user"
su test "entra como usuario test"
exit

userdel test

## pacman

### Sync -S


sudo pacman -S # instala paquetes 
sudo pacman -Syu # actualiza paquetes


#### Wifi and conections


networkmanager

sudo systemctl start NetworkManager