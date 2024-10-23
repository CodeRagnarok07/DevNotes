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

El "binding" en JavaScript se refiere a cómo se asocia el valor de `this` dentro de una función. El valor de `this` puede depender de cómo y dónde se llama la función. Aquí tienes un desglose:

### Binding Explícito

Puedes usar métodos como `.call()`, `.apply()`, o `.bind()` para asignar explícitamente el valor de `this`.

javascript

```
function saludar() {
    console.log("Hola, " + this.nombre);
}

const persona = { nombre: "Carlos" };

saludar.call(persona); // "Hola, Carlos"
```

### Binding Implícito

Ocurre cuando llamas a una función como método de un objeto. `this` se asocia automáticamente al objeto que contiene el método.

javascript

```
const objeto = {
    nombre: "María",
    saludar: function() {
        console.log("Hola, " + this.nombre);
    }
};

objeto.saludar(); // "Hola, María"
```

### Binding de Nuevo (new binding)

Cuando usas el operador `new` para crear una instancia de un constructor, `this` se asocia al nuevo objeto creado.

javascript

```
function Persona(nombre) {
    this.nombre = nombre;
}

const persona = new Persona("Luis");
console.log(persona.nombre); // "Luis"
```

### Binding de Defecto

En modo estricto (`strict mode`), `this` será `undefined` si no está explícitamente asociado. En modo no estricto, será el objeto global (`window` en navegadores).

javascript

```
function saludar() {
    "use strict";
    console.log(this); // undefined
}

saludar();
```

El binding es clave para entender el comportamiento de `this` en diferentes contextos de ejecución. ¡Es una parte fascinante de la magia que hace que JavaScript funcione!
