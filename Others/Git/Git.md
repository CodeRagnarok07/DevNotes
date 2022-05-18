# Estatus en vscode

U =     sin segimiento
A =     añadido
UU =    union con conflictos resuelta
M =     modificado

# Comandos Git

`ls` ⇒ ver directorios
`pwv`  ⇒ para ver el directorio actual

`git init`  ⇒  para comenzar el control de versiones
`git status` ⇒ Revisa los arivos agregados
`git status -s`   ⇒ solo muestra los modificados

`git add - archivo`     ⇒ seguido el nombre de un archivo
`git add --all`   ⇒ para agregar todo
`git add .` ⇒ agrega todo

`git commit -m "comentario"` ⇒ para evitar el editor
`git diff index.html` -  ==> comprueba las modificaciones en verde


### Agregar usuario

`git config --global user.email` ⇒ el email de quien hace el cambio
`git config --global user.name`  ⇒ configura la persona que hace el cambio
`git config --list` ⇒ lista de datos


## Remote

## Git Pull
`git remote add origin "url"`  ⇒ agrega la direcion

`git clone "url"` ⇒ crea una copia de un proyecto
`git pull`    == copia desde el github a los archivos local
`git fecht`   == pregunta primero antes de actualizar el archivo local


## Git Push

`git push origin "branch"`  ==los sube al repositorio desde un branch

`git push -u origin "main"` ==sube los archivos

`git push origin --delete "master"`

`git push --force master` ⇒ sincroniza las versiones eliminando los commits que se perdieron en el merge [daña el trabajo del grupo ]

## Crear o eliminar un Branch

`git branch`             ⇒ ver accede o crea un proyecto alternativo a partir

`git branch "nombre"`  ⇒ crea otra rama

`git branch -m master main` ⇒ para de cambiar master a main

`git branch -M main`     ⇒  acede directamente a main

`git checkout "nombre"`    CHANGE  ⇒ para cambiar de branch []

`git branch -d nombre`  ⇒  DELETE  Elimina la rama nombre  []

`git merge nombre`  ⇒ FUSION [ Siempre ubicarse en la rama “principal” para hacer la fusion

desde el principal combinarlo con otra rama y actualizr la pricipal
*si las dos ramas tienen modificaciones da opción a cambiarlo*
*[rama entrante] es la rama secundaria*



## Commits

`git log` ⇒ Ver todos los commits por codigo

`git log --oneline`  =describe cada commit

git checkout id commit  ⇒ Vuelve a ese commit y Preserva las resvisiones


# Flujo de trabajo reset

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4f721942-1d43-456b-9064-63f78fb62467/Untitled.png)

### hard:
vuelve a un commit y actualiza el espacio de trabajo eliminando los comits posteriores
    
    `git reset --hard [codigoDelComit]`  ==volver a un comit anterior espesifico
    
    `git reset --hard HEAD~3`  ⇒ si no quieres mantener los cambios y volver 4 commits antes 
    
    [ restablece todo ] sin hacer pull para poder volver a los anteriories commit
    
    `git reset id commit`  ⇒ Vuelve a ese commit y Descarta las resvisiones
    
### soft: 
vuelve a un commit y mantiene los comits posteriores
    
`git reset --soft HEAD` ⇒ si quieres volver un cambio antes
    
### mixed: 
vuelve a un commit y actualiza el espacio de trabajo mantiene los comits posteriores
    
`git reset [--mixed] HEAD~3` ⇒ mantener los cambios realizados y volver 4 commits antes
    

# Tags Versión alternativa del proyecto

puede ser una version alternativa del proyecto con los mismos branch y commits

`git tag nameversion -m "descripcionVersion01"`
`git push --tag`

