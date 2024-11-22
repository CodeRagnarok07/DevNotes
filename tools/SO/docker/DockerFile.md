


Comandos para docker build

| flag            | descripcion                                                                                   |
| --------------- | --------------------------------------------------------------------------------------------- |
| `-t, --tag`:    | Etiqueta la imagen con un nombre.                                                             |
| `-f, --file`:   | Nombre del archivo Dockerfile (por defecto es `Dockerfile`).                                  |
| `--build-arg`:  | Establece variables de construcción.                                                          |
| `--cache-from`: | Imágenes para considerar como caché.                                                          |
| `--no-cache`:   | No usa la caché al construir la imagen.                                                       |
| `--pull`:       | Siempre intenta descargar una versión más reciente de las imágenes base.                      |
| `--rm`:         | Elimina el contenedor intermedio después de una construcción exitosa (por defecto es `true`). |
| `--force-rm`:   | Elimina los contenedores intermedios incluso si la construcción falla.                        |
| `--compress`:   | Comprime el contexto de construcción usando gzip.                                             |
| `--label`:      | Añade una etiqueta a la imagen.                                                               |
| `--network`:    | Establece el modo de red para la construcción.                                                |
| `--target`:     | Establece la etapa de construcción objetivo.                                                  |
| `--squash`:     | Aplana la imagen resultante en una sola capa.                                                 |
| `--platform`:   | Establece la plataforma de la imagen (ej. `linux/amd64`).                                     |