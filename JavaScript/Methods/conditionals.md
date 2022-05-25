Condicionales

```jsx
!    |diferente o lo contrario
no   |queNoSea    
==   |igual       
===  |Estrictamente igual
!=   |diferente
!==  |Estricta diferente
```

Doble condición

```jsx
una_o_otra : "||, OR",
una_y_otra : "&&, AND"
```

---

Uso de If, else, else if

```jsx
const condicion = () =>{
if (undefined === null){
console.log("undefine siempre esta declarada, y no es igual a null estrictamente")
}
else if(undefined == null){
console.log("undefine es igual a null pero no estrictamente")
}
else{
console.log("nada")
}
}
```

---

Comprobación

```jsx
false && console.log("no es true")
```

Comprobacion con opciones

```jsx
false || true && console.log("se cumple")
```

---

Pregunta

```jsx
null == undefined ?
// si se cumple =
console.log('se cumple la condicion') 
: // si no se cumple =
console.log('no se cumple la condicion')
```