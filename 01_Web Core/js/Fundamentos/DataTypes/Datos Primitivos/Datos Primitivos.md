

En [JavaScript](https://developer.mozilla.org/es/docs/Glossary/JavaScript), un **primitive** (valor primitivo, tipo de dato primitivo) son datos que no son un [objeto](https://developer.mozilla.org/es/docs/Glossary/Object) y no tienen [métodos](https://developer.mozilla.org/es/docs/Glossary/Method). 

Hay 6 tipos de datos primitivos:
- [string](https://developer.mozilla.org/es/docs/Glossary/String)
- [number](https://developer.mozilla.org/es/docs/Glossary/Number)
- [bigint](https://developer.mozilla.org/es/docs/Glossary/BigInt))
- [boolean](https://developer.mozilla.org/es/docs/Glossary/Boolean)
- [undefined](https://developer.mozilla.org/es/docs/Glossary/Undefined) 
- [symbol](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Symbol).


También hay [null](https://developer.mozilla.org/es/docs/Glossary/Null)  que aparentemente es primitivo)  pero de hecho es un caso especial para cada [`Object`](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Object): y cualquier tipo estructurado se deriva de `null` por la [Cadena de prototipos](https://developer.mozilla.org/es/docs/Learn/JavaScript/Objects/Classes_in_JavaScript).


## Mutabilidad

> [! ] Todos los primitivos son **inmutables**, es decir, no se pueden modificar. 
 Es importante no confundir un primitivo en sí mismo con un valor primitivo asignado a una variable. Se puede reasignar un nuevo valor a la variable, pero el valor existente no se puede cambiar de la misma forma en que se pueden modificar los objetos, los arreglos y las funciones.

> [!warning ] Ejemplo 
>
> ```js
// El uso de un método de cadena no modifica la cadena
var bar = "baz";
console.log(bar); // baz
bar.toUpperCase();
console.log(bar); // baz
> 
// El uso de un método de arreglo muta el arreglo
var foo = [];
console.log(foo); // []
foo.push("plugh");
console.log(foo); // ["plugh"]
>
// La asignación le da al primitivo un nuevo valor (no lo muta)
bar = bar.toUpperCase(); // BAZ
>
>  ```


Un primitivo se puede reemplazar, pero no se puede modificar directamente.







%% Begin Waypoint %%
- **[[Datos Primitivos]]**
	- [[Datos Primitivos]]
	- [[number]]
	- [[string]]
	- [[undefined]]

%% End Waypoint %%




## ref

- https://developer.mozilla.org/es/docs/Glossary/Primitive
