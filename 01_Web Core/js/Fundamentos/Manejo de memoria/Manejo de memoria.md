---
tags:
  - nota-permanente
Lang: 
focus: false
title: Manejo de memoria
description: 
sidebar: 
public: false
note-type: blog-startlight
---
# Manejo de memoria

**La gestión de memoria en [[Areas/Backlog/DevNote/01_Web Core/js/js|JavaScript]]se refiere a cómo el lenguaje de programación gestiona y libera recursos de memoria utilizados por una aplicación.**


## Heap (montón):
Se utiliza para almacenar objetos y datos que necesitan más memoria. La memoria heap es menos organizada que la stack y puede contener objetos más grandes y complejos. Aquí es donde entra en juego el concepto de “pasar por referencia”, ya que los objetos en JavaScript se almacenan en la memoria heap.
El montón almacena objetos de forma no estructurada y se gestiona automáticamente por el motor V8.
Los objetos en el montón persisten incluso después de que se eliminen los marcos de pila.



---
```js
// Almacenamiento en stack
let nombre = 'Juan'; // Cadena (primitivo) almacenada en stack

// Almacenamiento en heap
let persona = {
  nombre: 'Juan', // Propiedad (almacenada en heap)
  edad: 30
};

function saludar() {
  let saludo = 'Hola'; // Variable local (almacenada en stack)
  console.log(saludo + ', ' + nombre);
}

saludar(); // "Hola, Juan"
```


La cadena `nombre` y la variable `saludo` están en la stack, mientras que el objeto `persona` está en la heap. La gestión de la memoria y el recolector de basura (Garbage Collector) en JavaScript trabajan detrás de escena para liberar memoria automáticamente cuando ya no es necesaria, lo que ayuda a evitar fugas de memoria y otros problemas relacionados.


#### Datos primitivos en funciones

 Los datos primitivos son inmutables, lo que significa que una vez creados, su valor no puede cambiar. Cuando pasas un dato primitivo a una función, se pasa una copia del valor, por eso se dice que se pasan por valor.

Por otro lado, los objetos son mutables, y cuando se pasan a una función, se pasa una referencia a su ubicación en la memoria. Esto permite que las funciones puedan modificar el contenido del objeto original.

La diferencia radica en cómo se almacenan y gestionan en la memoria.

```js
// Primitivos (se pasan por valor)
function cambiarValor(x) {
  x = 42;
}

let a = 10;
cambiarValor(a);
console.log(a); // Imprime 10, porque 'a' no cambia

// Objetos (se pasan por referencia)
function cambiarPropiedad(obj) {
  obj.propiedad = 42;
}

let b = { propiedad: 10 };
cambiarPropiedad(b);
console.log(b.propiedad); // Imprime 42, porque 'b' cambia
```


# manejo de la memoria


### Memorización
La memorización en JavaScript es una técnica de optimización que consiste en almacenar los resultados de funciones costosas en una caché, para evitar recalcularlos cada vez que se necesitan. Esto puede mejorar significativamente el rendimiento de un programa, especialmente cuando se trabajan con funciones que requieren un tiempo de cálculo significativo

> usado por algunas funciones de react como useCallback y useMemo

#### Técnicas de memorización
1. **Objeto caché**: Se crea un objeto vacío que almacena los resultados de las funciones costosas. Luego, se verifica si el resultado ya está almacenado en el objeto caché antes de calcularlo nuevamente.
2. **Claves de identificación**: Se utilizan claves de identificación únicas para almacenar y recuperar los resultados en el objeto caché.
3. **Actualización de la caché**: Se actualiza la caché cuando se cambia el estado del programa o se producen cambios en los datos.

##### Fibonacci
Probemos algo simple como generar una secuencia de fibonacci. Una secuencia de Fibonacci es donde cada dígito es la suma de los dos elementos anteriores, 
0, 1, 1, 2, 3, 5, 8, 12 …

```js
const fibonacci = num => {
	if (num < 2) return num;
	const result = fibonacci(num - 1) + fibonacci(num - 2);
	console.log(result) // se imprime el numero de num*2
	return result

};

for (let i = 0; i < 1000; i++) {
	console.log(fibonacci(i));
}
```

Lo anterior, se acaba el stack de llamadas en aproximadamente 3 minutos.


```js
const fibonacciMemo = (num, memo) => {
  memo = memo || {}; //la memoria no se libera por que se hace referencia en el algoritmo
  if (memo[num]) return memo[num];
  if (num < 2) return num;
  return memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo);
};
```



### Migración hacia JavaScript de memoria estática  (no resuelto)

**Static Memory JavaScript** es una técnica que implica [asignar previamente](http://en.wikipedia.org/wiki/Sawtooth_wave), al inicio de tu app, toda la memoria que se necesitará durante su vida útil y administrarla durante la ejecución a medida que ya no se necesitan los objetos. Para alcanzar este objetivo, podemos seguir algunos pasos sencillos:

1. Instrumenta tu aplicación para determinar cuál es la cantidad máxima de objetos de memoria activos necesarios (por tipo) para una variedad de situaciones de uso.
2. Vuelve a implementar tu código para asignar previamente esa cantidad máxima y, luego, recupérala/libera de forma manual en lugar de ir a la memoria principal.

Alcanzar el 1er lugar requiere que hagamos un poco de 2, así que empecemos por ahí.


### Grupo de objetos
 
En pocas palabras, la [agrupación de objetos](http://en.wikipedia.org/wiki/Object_pool_pattern) es el proceso de retener un conjunto de objetos sin usar que comparten un tipo. Cuando necesites un objeto nuevo para tu código, en lugar de asignar uno nuevo desde el [montón de memoria](https://en.wikipedia.org/wiki/Memory_management) del sistema, reciclarás uno de los objetos que no se usen del grupo. Una vez que el código externo se completa con el objeto, en lugar de liberarlo a la memoria principal, este vuelve al grupo. Debido a que el objeto nunca se [deshace de la referencia](http://en.wikipedia.org/wiki/Reference_(computer_science)) (es decir, se borra) del código, no se recolectará. **El uso de grupos de objetos permite que el programador tenga el control de la memoria, lo que reduce la influencia del recolector de elementos no utilizados en el rendimiento.**

Debido a que una aplicación mantiene un conjunto heterogéneo de tipos de objetos, el uso adecuado de los grupos de objetos requiere que tengas un grupo por tipo que experimente una alta deserción durante el tiempo de ejecución de tu aplicación.

```js
var newEntity = gEntityObjectPool.allocate();
newEntity.pos = {x: 215, y: 88}; 

//..... do some stuff with the object that we need to do

gEntityObjectPool.free(newEntity); //free the object when we're 
donenewEntity = null; //free this object reference
```

Para la gran mayoría de las aplicaciones, con el tiempo llegarás a algún nivel en términos de la necesidad de asignar objetos nuevos. En varias ejecuciones de tu aplicación, deberías poder comprender bien cuál es este límite superior y puedes asignar previamente esa cantidad de objetos al comienzo de tu aplicación.




- https://web.dev/articles/speed-static-mem-pools?hl=es-419
- https://developer.mozilla.org/es/docs/Web/JavaScript/Memory_management