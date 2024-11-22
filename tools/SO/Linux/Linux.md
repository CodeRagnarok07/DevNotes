

### Linea de comandos



··· personalizacion xfce

https://www.xfce-look.org/
https://aur.archlinux.org/packages/flat-remix


# Pacaquetes basicos


## `lsb-release`

`lsb-release` es un paquete en sistemas basados en Debian y Ubuntu que proporciona información sobre la distribución del sistema operativo. Incluye un comando llamado `lsb_release` que se utiliza para obtener detalles como el nombre de la distribución, la versión y el identificador de codename.

Aquí hay algunos ejemplos de cómo se puede usar `lsb_release`:

- `lsb_release -a`: Muestra toda la información disponible sobre la distribución.
- `lsb_release -d`: Muestra la descripción de la distribución.
- `lsb_release -r`: Muestra la versión de la distribución.
- `lsb_release -c`: Muestra el codename de la distribución.

En el contexto de tu script, `lsb_release -rs` se usa para obtener la versión de la distribución, lo cual es útil para determinar la URL correcta del repositorio de Microsoft SQL Server.

Para instalar `lsb-release`, puedes usar el siguiente comando: