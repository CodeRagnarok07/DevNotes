


·· comando de iniciacion
"sin comillas todo"

qemu-system-x86x64

-m 2G 		· memoria ram
-smp 2    	· nucleos
--enable-kvm 	·
--name nombre   · name de la maquina
-boot d 
-hda  "ruta del disco"
-cdrom "ruta del iso"

·· creacion de imagenes

qemu-img 
create 				· ocpion de creacion
-f      			· 
qcow2 "nombre del disco" 	· formato y nombre del disco     
20g 				· espacio del disco


qemu-img info "nombre del disco creado"

qemu-system-x86_64 --enable-kvm -m 2G -smp 2 -boot d -cdrom /home/rag/box/kali-linux-2024.3-live-amd64.iso




··· personalizacion xfce


https://www.xfce-look.org/

https://aur.archlinux.org/packages/flat-remix
