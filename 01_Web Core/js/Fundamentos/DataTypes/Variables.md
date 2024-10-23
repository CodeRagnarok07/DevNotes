
### Variables


##### 1.- VAR

- se registran en el documento global 
- puede declararse nuevamente
- y se puede modificar su valor


```jsx
var variable = ""
```

2.- LET

```jsx
let variable = "no se puede declarar otra ves "
variable = "pero si se puede modificar su valor"

if (true){
    let variable = "se puede redefinir dentro de un if por que no es global"
    console.log(variable )
}

```

3.- CONST

```js
const constanteas = "no se puede modificar siempre es constante"
const array = ["se", "puede", "agregar", "por", "medio", "de" ]
array.push("sus propiedades mutables")
```

---

#### typeof 

imprime el tipo de dato 

```js
console.log(typeof variables.Numero)
```


