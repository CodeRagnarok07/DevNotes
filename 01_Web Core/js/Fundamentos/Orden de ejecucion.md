---
tags:
  - nota-permanente
Lang: 
focus: false
title: Orden de ejecucion
description: 
sidebar: 
public: false
note-type: blog-startlight
---
## El Event Loop

El Event Loop (ciclo de eventos) es un componente crucial en el runtime de JavaScript, responsable de la ejecución asíncrona de código y el manejo de eventos. Es como un organizador infatigable que mantiene el flujo de trabajo, garantizando que las tareas se ejecuten de manera eficiente y sin bloquear el navegador.

el event loop Funciona como un bucle que verifica constantemente si hay tareas pendientes en la cola de mensajes (también conocida como message queue).

JavaScript es un lenguaje de programación de un solo subproceso, lo que significa que ejecuta una tarea a la vez. (bloqueante)  Sin embargo, gracias al modelo de concurrencia basado en el [[Event loop|Event loop]]  puede lograr el efecto de ejecución no bloqueante.


### 1. **Call Stack**:

la **call stack** maneja la ejecución de funciones y su [[Areas/Backlog/DevNote/01_Web Core/js/runtime/Manejo de memoria/contexto de ejecución]] de manera ordenada y secuencial, mientras que la **message queue** maneja eventos que esperan ser procesados una vez que la call stack esté vacía. 
Tambien conocida como Pila de Llamadas
- La call stack es una estructura de datos donde se registran las llamadas a funciones.
- Cuando se llama a una función, se añade un contexto de ejecución a la pila (stack).
- Cuando una función termina, su contexto se elimina de la pila.
- Esencialmente, la call stack sigue un orden LIFO (Last In, First Out), lo que significa que la última función llamada es la primera en terminar su ejecución.

La pila de llamadas es una estructura de datos que rastrea las llamadas a funciones en un programa.
Cada vez que se llama a una función, se agrega un marco de pila que contiene referencias a los argumentos y variables locales de esa función.
Cuando una función se completa, su marco se elimina de la parte superior de la pila.
El orden de ejecución sigue el principio “último en entrar, primero en salir” (LIFO).
Ejemplo: Si llamamos a la función bar, se crea un marco de pila para ella, y si bar llama a foo, se crea otro marco de pila para foo encima del de bar.
el registro guarda en memoria los datos de el [execution context](#execution-context) y su entorno léxico durante la ejecución
guarda el orden de ejecucion de las funciones, la creacion y destrucion del entorno lexico y su registro en memoria


### 2. **Message Queue**: 
- Tambien llamada 
	- Cola de eventos
	- Task Queue
	- message Queue
	- Cola de Mensajes
	- cola de tareas

- Procesa funciones asincronas bloqueantes
- La message queue es una lista de mensajes (o eventos) que han sido enviados para ser procesados.
- Los mensajes en la cola se procesan siguiendo un orden FIFO (First In, First Out), lo que significa que el primer mensaje en entrar es el primero en ser procesado.
- Los eventos en la cola son atendidos por el "event loop", que chequea si la call stack está vacía antes de procesar el siguiente evento.
La cola de mensajes es una lista de mensajes que deben procesarse.
Cada mensaje tiene una función asociada que se ejecutará para manejarlo.
Durante el event loop, el motor de JavaScript procesa los mensajes en la cola, comenzando por el más antiguo.
Cuando se procesa un mensaje, se elimina de la cola y se llama a la función correspondiente.
Ejemplos de tareas en la cola incluyen setTimeout, fetch y eventos del DOM.

---
Juntas, la call stack y la message queue permiten que JavaScript pueda manejar operaciones asíncronas de manera eficiente.

```js
console.log('Inicio');

// Función asincrónica (utiliza setTimeout)
setTimeout(() => {
  console.log('Operación asíncrona');
}, 0);

// Función síncrona
console.log('Fin');
```

En este ejemplo, JavaScript sigue estos pasos:

1. La llamada a `console.log('Inicio')` se añade a la call stack y se ejecuta. Luego se elimina de la stack.
2. La llamada a `setTimeout()` se añade a la call stack. `setTimeout()` configura un temporizador y se registra el callback para que se ejecute después de 0 milisegundos, pero la función no se ejecuta de inmediato. El callback se coloca en la message queue y `setTimeout()` se elimina de la stack.
3. La llamada a `console.log('Fin')` se añade a la call stack y se ejecuta. Luego se elimina de la stack.
4. La call stack ahora está vacía, por lo que el event loop toma el callback de la message queue y lo añade a la call stack.
5. La llamada a `console.log('Operación asíncrona')` se ejecuta y se elimina de la stackl.


## Orden de Ejecución de las funciones:

#### 1.- Código Síncrono: 
El código síncrono se ejecuta línea por línea, bloqueando el Event Loop hasta que finalice. 
```js
console.log('1. Ingreso al código síncrono'); // Se ejecuta inmediatamente
function mostrarNombre(nombre) {
  console.log('2. Función síncrona:', nombre);
}
mostrarNombre('Juan'); // Se ejecuta inmediatamente
console.log('3. Salida del código síncrono'); // Se ejecuta después de la función
```


#### 2.-  Eventos del DOM: 
Cuando ocurre un evento, se agrega a la cola de eventos y espera su turno para ser procesado. 

```js
document.addEventListener('click', function() {
  console.log('4. Evento click detectado'); // Se ejecuta cuando se hace clic en el elemento
});

console.log('5. Código posterior al evento'); // Se ejecuta antes del evento click
// Simulando un clic
document.dispatchEvent(new Event('click'));
```

#### 3.-  Tareas Asíncronas:  (Qeueu)
Las tareas asíncronas se delegan al pool de hilos o a un web worker y se ejecutan en segundo plano. El Event Loop las programa para que se ejecuten en un momento posterior mediante callbacks. 
```js
console.log('6. Inicio de tarea asíncrona'); // Se ejecuta inmediatamente

setTimeout(function() {
  console.log('8. Tarea asíncrona completada'); // Se ejecuta después de 2 segundos
}, 2000);

console.log('7. Código posterior a la tarea asíncrona'); // Se ejecuta inmediatamente
```

#### 4.- Callbacks: (Qeueu)
Las callbacks se ejecutan cuando las tareas asíncronas se completan, permitiendo que el código continúe su flujo. 
```JS
const promesa = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('9. Promesa resuelta'); // Se ejecuta después de 2 segundos
  }, 2000);
});

promesa.then(function(resultado) {
  console.log(resultado); // Se ejecuta después de que la promesa se resuelva
});

console.log('10. Código posterior a la promesa'); // Se ejecuta inmediatamente
```

## Otros sistemas de ejecución

- Pool de Hilos: Un grupo de hilos de ejecución que se encargan de las tareas asíncronas computacionalmente intensivas.
- Web Workers: Hilos de ejecución independientes que permiten ejecutar código JavaScript en segundo plano sin bloquear el hilo principal.
- Callback: Funciones que se ejecutan cuando una tarea asíncrona se completa.
- API de Asincronía: Proporciona mecanismos para manejar tareas asíncronas, como setTimeout, XMLHttpRequest y Promises.



### SRC

-  [Event loop interactivo](https://vault-developer.github.io/event-loop-explorer/)