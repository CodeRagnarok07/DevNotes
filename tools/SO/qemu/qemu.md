[Introduction — QEMU documentation](https://www.qemu.org/docs/master/system/introduction.html)

### Ejecucion

| Descripcion           | parametro                                 | valores | ej                         |     |
| --------------------- | ----------------------------------------- | ------- | -------------------------- | --- |
| comando de iniciacion | `qemu-system-x86x64`                      |         |                            |     |
| memoria ram           | `-m`                                      | 2G      | `-m 2G `                   |     |
| nucleos               | `-smp`                                    | 2,1,3,4 | `-smp 2`                   |     |
|                       | `--enable-kvm`                            |         |                            |     |
| name de la maquina    | `--name`                                  |         | `--name nombre`            |     |
|                       | `-boot`                                   | d       | `-boot d`                  |     |
| ruta del disco        | `-hda`                                    | /path   |                            |     |
| ruta del iso          | `-cdrom`                                  | /path   |                            |     |
|                       | ``                                        |         |                            |     |


### Disco

| Descripcion           | parametro                                 | valores | ej                         |     |
| --------------------- | ----------------------------------------- | ------- | -------------------------- | --- |
| Creación de disco     | ###############                           | ######  | ############               |     |
|                       | `qemu-img create  `                       |         |                            |     |
|                       | `create `                                 |         |                            |     |
| "nombre del disco"    | `qcow2`                                   |         | formato y nombre del disco |     |
| espacio del disco     | `20g`                                     |         | `20g`                      |     |
|                       | ``                                        |         |                            |     |
|                       | ``                                        |         |                            |     |


### Info

| Descripcion | parametro                                 | valores | ej  |     |
| ----------- | ----------------------------------------- | ------- | --- | --- |
| Info        | ###############                           |         |     |     |
|             | `qemu-img info "nombre del disco creado"` |         |     |     |
|             | ``                                        |         |     |     |
|             | ``                                        |         |     |     |
|             | ``                                        |         |     |     |
|             | ``                                        |         |     |     |
|             | ``                                        |         |     |     |
|             | ``                                        |         |     |     |
|             |                                           |         |     |     |
|             |                                           |         |     |     |



### Usos

Crear disco
```
qemu-img create -f qcow2 disk.qcow2 20g
```

ver disco
```
qemu-img info disk.qcow2
```

Montar iso
```
qemu-system-x86_64 -m 2G -smp 2 --enable-kvm -name 'win10' -boot d -cdrom '/path-to-the.iso'
```

mintar iso en disco
```
qemu-system-x86_64 -m 2G -smp 2 --enable-kvm -name 'win10' -boot d -hda disk.qcow2 -cdrom '/path-to-the.iso'
```

levantar solo el disco
```
qemu-system-x86_64 -m 2G -smp 2 --enable-kvm -name 'win10' -boot d -hda disk.qcow2
```



# SRC

- [calnal de linux y virtualizacion](https://www.youtube.com/watch?v=hG0uougZ_J0&list=PLxJguiVqgxl8J0SkbeUW9z0kby5thRNSp)


es posible crear máquinas virtuales con QEMU que utilicen recursos de manera dinámica, similar a cómo lo hace WSL (Windows Subsystem for Linux). Aquí te dejo algunos puntos clave:

1. **Discos dinámicos**: Puedes crear discos virtuales que crecen dinámicamente según la necesidad. Esto significa que el disco virtual solo ocupará el espacio que realmente se está utilizando, en lugar de reservar todo el espacio asignado desde el principio.
    
2. **Asignación de memoria**: Aunque QEMU no tiene una funcionalidad exacta como la de WSL para la memoria dinámica, puedes ajustar la cantidad de memoria asignada a la máquina virtual según tus necesidades. Además, puedes usar técnicas como el "ballooning" de memoria en combinación con KVM para ajustar dinámicamente la memoria disponible para las máquinas virtuales.
    
3. **CPU y otros recursos**: Puedes configurar QEMU para que utilice recursos de CPU de manera flexible, permitiendo que la máquina virtual utilice más o menos CPU según la carga de trabajo actual.
    

Para implementar estas configuraciones, necesitarás ajustar los parámetros de QEMU y posiblemente utilizar herramientas adicionales como libvirt para una gestión más avanzada. 
