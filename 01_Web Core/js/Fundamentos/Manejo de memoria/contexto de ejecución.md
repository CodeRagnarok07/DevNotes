---
tags:
  - nota-permanente
Lang: 
focus: false
title: contexto de ejecución
description: 
sidebar: 
public: false
note-type: blog-startlight
---
## Contexto de ejecución 

Es un objeto literal de javascript que almacena la informacion de las variable y funciones en la [[Areas/Backlog/DevNote/01_Web Core/js/runtime/Manejo de memoria/Stack|Memoria Stack]]

El execution context es el entorno en el que se ejecuta el código. Cada vez que se llama a una función, se crea un nuevo execution context. Contiene tres partes principales:
1. **Variable Object**: Contiene todas las variables, funciones y parámetros locales.
1. **Scope Chain**: Incluye la variable object y todas las variables de sus padres o entorno lexico asociado
3. **This**: Referencia al objeto actual.

Se definen dos tipos de contexto de ejecución
- Global Execution Context (GEC) o Scope Global
- Function Execution context (FEC)


Es un objeto literal del javascript que contine la informacion clave valor sobre el entorno de ejecución y se genera en la fase de creación del mismo la información que contiene es

```js
GEC = {
	scope             : "global",
	funcion1definida  : function(){}
}
FEC1 = {
	scope : "function",
	vars  : "variable definida"
	ECparent: "GEC"
} 
```


El contexto léxico en JavaScript se establece durante dos fases clave en el ciclo de vida de ejecución del código:

1. **Fase de Creación (Compilation phase)**: Aquí, el intérprete de JavaScript recorre el código en busca de declaraciones de variables y funciones. Durante esta fase, se construyen los contextos léxicos y se registran las variables y funciones en esos contextos. Esto es cuando ocurre el hoisting, levantando las declaraciones al principio de su contexto.
    
2. **Fase de Ejecución (Execution phase)**: En esta fase, el código se ejecuta línea por línea, y las variables se inicializan con los valores asignados. El contexto léxico permite a las funciones acceder a las variables y funciones en su alcance léxico.


### Fases del context de ejecución

#### 1. **Fase de Creación (Compilation phase)**: 

Aquí, el intérprete de JavaScript recorre el código en busca de declaraciones de variables y funciones. Durante esta fase, se construyen los contextos léxicos y se registran las variables y funciones en esos contextos. Esto es cuando ocurre el hoisting, 
##### Hoisting
El hoisting es un comportamiento en JavaScript en el cual las declaraciones de variables y funciones son “elevadas” al comienzo de su contexto de ejecución durante la fase de compilación

A diferencia de `var`, las declaraciones con `let` y `const` no se "hoistean" de la misma manera. Mientras que técnicamente también son elevadas al inicio de su contexto, no pueden ser accedidas antes de su declaración en el código. Esto es conocido como el "Temporal Dead Zone" (TDZ).

```js
console.log(miVariable); // ReferenceError: miVariable is not defined
let miVariable = 5;
```

En este caso, intentar acceder a `miVariable` antes de su declaración con `let` resulta en un `ReferenceError`. Lo mismo aplica para `const`. Esto introduce un comportamiento más predecible y seguro en comparación con `var`.





#### 2. **Fase de Ejecución (Execution phase)**:
En esta fase, el código se ejecuta línea por línea, y las variables se inicializan con los valores asignados. El contexto léxico permite a las funciones acceder a las variables y funciones en su alcance léxico. en esta fase sucede el [[Areas/Backlog/DevNote/01_Web Core/js/runtime/Manejo de memoria/Binding|Binding]]




#### 3.- Liberación (Garbage Collection)

JavaScript usa un proceso llamado **garbage collection** para liberar memoria. El **garbage collector** busca objetos que ya no tienen referencias activas y los elimina de la memoria. Esto se hace principalmente con el algoritmo de **marcado y barrido** (mark-and-sweep). En resumen, marca todas las referencias alcanzables y luego barre las no marcadas, liberando la memoria ocupada por estas.




## Scope o Lexical Context 


se refiere al alcance de las variables definido por la estructura del código durante la fase de creación. Es estático y se establece cuando se define la función, no cuando se ejecuta. Define qué variables y funciones están accesibles basándose en dónde se declararon en el código fuente.

El contexto léxico define el alcance de las variables. Depende de dónde se declara la función o variable en el código. JavaScript utiliza alcance léxico, lo que significa que las funciones acceden a variables desde su contexto de declaración y no desde su contexto de ejecución.

El contexto léxico es un concepto fundamental en JavaScript. Básicamente, define el ámbito donde las variables y funciones son accesibles según dónde fueron declaradas en el código fuente, no según dónde se ejecutan. Esto significa que una función puede acceder a variables dentro de su ámbito léxico, que se determina al momento de su definición.





