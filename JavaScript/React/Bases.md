
# Variables de entorno en react
    
    
1. Crea el archivo .env bajo el siguiente formato

```jsx
REACT_APP_API_KEY_FIREBASE=sdsa65d576a5w67d5s 
```

- REACT_APP_ siempre al principip
- toda la variabel debe estar en mayusculas
- la variable puede estar en Sting pero sin espacios al final ni comas
2. Call Var

```jsx
apiKey: process.env.REACT_APP_API_KEY_FIREBASE,
```
