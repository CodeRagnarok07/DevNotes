### Configuracion de la api

`firestore.js`
```jsx
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

import { getFirestore } from "firebase/firestore";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCGhzGO-BkA7RFl4jM3rVcqJstVitMlyeo",
  authDomain: "my-apps-759f0.firebaseapp.com",
  projectId: "my-apps-759f0",
  storageBucket: "my-apps-759f0.appspot.com",
  messagingSenderId: "877108099142",
  appId: "1:877108099142:web:3bebbbd3ec63d5961ab247",
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);
export const db = getFirestore(app);
```

### Configuración Firestore db

1. crea la base de datos en firestore, firecould 
2. `firestore`
    
Aqui se asignan los métodos query

```jsx
import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore"
const app = initializeApp(firebaseConfig);

const db = getFirestore(app); 
export default db
```