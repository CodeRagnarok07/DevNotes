### **While**

```js
while (i < conteo) {
  i++;
  if (i % 2 == 0 && i % 5 == 0) {
    document.write("bisbos" + i + "<br>");
  } else if (i % 2 == 0) {
    break; // detiene el ciclo
    document.write("bizz " + i + "<br>");
  } else if (i % 5 == 0) {
    continue; // equivalente a pass
    document.write("bozz" + i + "<br>");
  } else {
    document.write(i + "<br>");
  }
}
```

### Do While:

```js
do {
 console.log("primera ejecucion")
} while (!true); // si es true se volvera a ejecutar
```
> es útil para ejecutar el ciclo una ves solamente para impulsar el algoritmo
> ejecuta el ciclo una primera ves luego la condicion dice si se ejecuta de nuevo


### Switch

```jsx
switch (key) {
    case value:
        break;

    default:
        break;
        
}
```