### C**onfiguracion Deploy:**

1. descripción general del proyecto > Configuración > Proyect sttings
2. tus apps > Agrega
3. Firebase a tu app web >
4. nombre de la aplicación >
5. Aceptar
6. copiar la configuracion SDK en un archivo .js
7. Agregarlo al index.js

### i**nstalaciones**

```css
npm install firebase
npm install -g firebase-tools
```

### D**eploy firebase**

1. `npm install -g firebase-tools`
2. `firebase login`
3. `firebase init`
    1. `Y > 4hosting > slect proyecto> dist> Y`
4. `npm rum build`
5. firebase.json
    
    ```css
    "hosting"{
    "public" : "dist" => cambiar a build
    ....
    }
    ```
    
6. `firebase deploy`