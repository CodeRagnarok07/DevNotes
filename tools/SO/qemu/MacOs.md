
debian-ubuntu
```
sudo apt-get update && sudo apt-get install qemu-system qemu-system-x86 uml-utilities virt-manager git wget libguestfs-tools p7zip-full make dmg2img tesseract-ocr tesseract-ocr-eng genisoimage vim net-tools screen -y
```


```
cd ~
git clone --depth 1 --recursive https://github.com/kholia/OSX-KVM.git
cd OSX-KVM

sudo modprobe kvm; echo 1 | sudo tee /sys/module/kvm/parameters/ignore_msrs

# for Intel CPU
sudo cp kvm.conf /etc/modprobe.d/kvm.conf  
# for AMD CPU
sudo cp kvm_amd.conf /etc/modprobe.d/kvm.conf  

sudo usermod -aG kvm $(whoami)
sudo usermod -aG libvirt $(whoami)
sudo usermod -aG input $(whoami)

./fetch-macOS-v2.py

dmg2img -i BaseSystem.dmg BaseSystem.img

qemu-img create -f qcow2 mac_hdd_ng.img 10G

sudo ./OpenCore-Boot.sh


cd OSX-KVM
sudo ./OpenCore-Boot.sh

```


```
apk add git wget qemu-system-x86_64 dmg2img virt-manage libvirt-uml 7zip make dmg2img  tesseract-ocr tesseract-ocr-eng cdrkit net-tools net-tools
```


apk add git wget qemu-system-x86_64 dmg2img virt-manager libvirt-uml 7zip make dmg2img  tesseract-ocr tesseract-ocr cdrkit net-tools net-tools