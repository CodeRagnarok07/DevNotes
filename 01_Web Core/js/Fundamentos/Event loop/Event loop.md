---
title: El Event Loop
description: Un mecanismo fundamental para la ejecución no bloqueante.
sidebar:
  label: EventLoop
  order: 1
---






# El Event Loop 





## ¿Cómo funciona el Event Loop de JavaScript?

1. Cola de Eventos: El Event Loop mantiene una cola donde se almacenan los eventos que se generan, como clics del mouse, solicitudes de red o temporizadores.
3. Procesamiento de Eventos: El Event Loop toma un evento de la cola y lo procesa, ejecutando el código asociado a ese evento.
4. Tareas Asíncronas: Si el evento involucra una tarea asíncrona, como una solicitud de red, el Event Loop la delega a un pool de hilos o a un web worker para que se ejecute en segundo plano.
5. Devolución de Control: Una vez que la tarea asíncrona se completa, el Event Loop recibe una notificación y programa una callback (función de retorno de llamada) para que se ejecute en un momento posterior.
6. Repetición del Ciclo: El Event Loop repite este proceso, tomando eventos de la cola, procesándose y manejando tareas asíncronas de manera no bloqueante.

## Componentes del Event Loop:

Cola de Eventos: Almacena los eventos que esperan ser procesados.




---
## ¿JavaScript es siempre un lenguaje bloqueante?
No, JavaScript no es un lenguaje inherentemente bloqueante. El Event Loop permite que el código JavaScript se ejecute de manera no bloqueante, mientras que las tareas asíncronas se ejecutan en segundo plano.

Sin embargo, existen algunas situaciones en las que el código JavaScript puede bloquear el Event Loop, como:

### Ejecución de código síncrono: 
La ejecución de código síncrono, como cálculos intensivos o bucles infinitos, puede bloquear el Event Loop y evitar que se procesen otros eventos, normalmente se puede solucionar con el uso de los web worker's.

### Uso inadecuado de APIs asíncronas: 
Si no se utilizan correctamente las callbacks o promesas, el código asíncrono puede bloquear el Event Loop y generar un comportamiento no deseado.


---
## ¿El Event Loop de JavaScript se comporta igual en todos los runtimes?

En general, el concepto fundamental del Event Loop es similar en la mayoría de los runtimes de JavaScript. Sin embargo, existen algunas diferencias sutiles en la implementación y optimización del Event Loop entre diferentes runtimes, como:

Eficiencia del pool de hilos: La eficiencia con la que se manejan las tareas asíncronas en el pool de hilos puede variar entre runtimes.
Optimizaciones específicas: Algunos runtimes pueden incluir optimizaciones específicas para ciertos tipos de eventos o tareas asíncronas.
Compatibilidad con APIs: La compatibilidad con APIs asíncronas específicas del navegador o del sistema operativo puede variar entre runtimes.

El Event Loop de JavaScript es un mecanismo esencial que permite la ejecución no bloqueante del código y el manejo eficiente de eventos. Si bien el concepto fundamental es similar en la mayoría de los runtimes, existen algunas diferencias sutiles en la implementación y optimización. JavaScript no es un lenguaje inherentemente bloqueante, pero la ejecución de código síncrono o el uso inadecuado de APIs asíncronas pueden bloquear el Event Loop.


Cuando una tarea asíncrona, como un setTimeout o una solicitud de red, se completa, se coloca en la cola de mensajes.

El event loop toma las tareas de la cola y las ejecuta en el orden en que llegaron, asegurando que el programa sea reactivo y no se bloquee mientras espera tareas largas.

característica agregada por los navegadores a JavaScript para realizar operaciones asincrónas
sin bloquear la ejecución, distribuyendo el orden de prioridad de la cola de tareas enviandolos al stack 
la prioridad es, tareas de js > tareas web Apis > micro tareas webApis



### Bucle de Eventos (Event Loop):
El event loop es un bucle constante que monitorea tanto la cola de mensajes como la pila de llamadas.

Si la pila no está vacía, el event loop espera hasta que lo esté y luego coloca la siguiente función de la cola en la pila.
Si la cola está vacía, el event loop espera a que llegue un nuevo mensaje.
El procesamiento de funciones continúa hasta que la pila esté nuevamente vacía.
En resumen, el event loop coordina la ejecución de tareas asíncronas en JavaScript, asegurando que las operaciones no bloqueen la aplicación y manteniendo la capacidad de respuesta






###  (Message Queue):

### Objetos en el Montón (Heap):
Los objetos en JavaScript se asignan en el montón, que es una región grande de memoria.


### cola de tareas
determina el orden de prioridad de ejecucion de las tareas web api
el orden de ejecucion de tareas del call stack es el siguiente 
1. tarea [javascript puro]
2. micro tarea web-api 
3. Tarea web-api

## las WEB API's
son características no propias de js si no del navegador que permiten manejar funciones mas lentas sin bloquear la ejecución
distribuye el orden de ejecución en la [cola de tareas]() dependiendo de su prioridad

- tarea
  - setTimeout | setInterval
  - fetch
  - Intersection DOM
- micro tarea
  - Promise
  - async await
  - process.NextTick
  - mutation observer
  - insertection


