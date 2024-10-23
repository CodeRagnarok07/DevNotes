---
tags:
  - nota-permanente
Lang: 
focus: false
title: Untitled
description: 
sidebar: 
public: false
note-type: blog-startlight
---
## Stack (pila):

Se utiliza para almacenar datos primitivos y variables locales dentro de funciones. La memoria stack es de acceso rápido y de tamaño limitado. Cada vez que se llama a una función, se crea un nuevo[[Areas/Backlog/DevNote/01_Web Core/js/runtime/Manejo de memoria/contexto de ejecución|Contexto de ejecución]]en la pila, y cuando la función termina, ese contexto se destruye por medio del .


## Stack overflow

En términos de programación, un “stack overflow” ocurre cuando el stack (la pila de llamadas) se llena más allá de su capacidad. Esto suele suceder debido a una recursión infinita, donde una función sigue llamándose a sí misma sin una condición de terminación correcta.


```js
function llamadaInfinita() {
    llamadaInfinita();
}

llamadaInfinita(); // Esto causará un stack overflow
```

El error de stack overflow es problemático porque consume memoria rápidamente, llevando al programa a un estado de falla. Es como si un trabajador tratara de apilar cajas en un almacén pequeño, pero sigue apilando sin parar hasta que todo se derrumba.