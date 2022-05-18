# CRUD Method 1
crear la api para los metodos**
    
```jsx
import { async } from "@firebase/util";
import {collection, getDocs, query, doc, addDoc, deleteDoc, updateDoc,} from "firebase/firestore";
import db from "./firebase";
```
    
## CREATE / ADD
    
```jsx
export const create = async (datos)=>{
await addDoc(collection(db, 'Todo'), {datos})
}

```

JSX

```jsx
// Create
    const [nuevaData, setNuevaData] = useState();
    const createNames = () => {
    if (nuevaData.First_name == null || nuevaData.Last_name == null) {
        openAlert("error", "required field");
    } else {
        create("Names", nuevaData);
        openAlert("success", "item saved");
        read();
    }
    };

```
    
## READ / GET
    
```jsx
export const getResultado = async ()=>{
const resultado = await getDocs(query(collection(db, 'Todo')));
return resultado;
}

```
JSX
    
```jsx

// Read
const [listData, setListData] = useState([]);
const read = () => {
getResultado("Names", setListData);
};
```
    
## UDATE / EDIT
    
```jsx
export const update = async (id, datos)=>{
await updateDoc(doc(db, 'persons', id), {datos})
console.log("archivo subido")
}
```

JSX

```jsx
// Update
    const [edictMode, setEdictMode] = useState(false);
    const startEdict = (a1, a2) => {
    setEdictMode(true);
    setNuevaData({ ...a1, id: a2 });
    };

    const saveEdict = () => {
    // si datos = null borrar o no hacer nada
    read();
    if (nuevaData.First_name === "" || nuevaData.Last_name === "") {
        openAlert("error", "required field");
    } else {
        update("Names", nuevaData.id, {
        First_name: nuevaData.First_name,
        Last_name: nuevaData.Last_name,
        });
        setEdictMode(false);
        openAlert("info", "item updated");
    }
    };

```
    
## DELETE

```jsx
export const remover = async (id)=>{
await deleteDoc(doc(db, 'Todo', id));
}
```

JSX

```jsx
const Delete = (id) => {
    remover("Names", id);
    openAlert("error", "item deleted");
    read();
    };

```


# CRUD Method 2
    
## GET

Import:

```jsx
import { collection, onSnapshot, orderBy, query } from 'firebase/firestore'
import { db } from '../../firebase'

```

const:

```jsx
const [skills, setSkills] = useState([])

    const getSkills = () => {
        const skillsRef = collection(db, "Skills");
        const q = query(skillsRef, orderBy("name", "desc"));
        onSnapshot(q, (snapshop) => {
            const qskills = snapshop.docs.map((doc) => ({
                id: doc.id, ...doc.data()
            }));
            setSkills(qskills)
            console.log(skills)
        })
    }

useEffect(() => {
        getSkills()
    }, [])
```

```html
{skills.length == 0 
?
<p> no hay skills </p>
:
skills.map((s) =>
<div key={s.id}>

</div>
```


## Post

Inport:

```

```

html

```

```

# - forms React
- form 2 with image in firebase

```jsx
const [formData, setFormData] = useState({
    name: "",
    description: "",
    image: "",
    createdAt : Timestamp.now().toDate() // funtion format date autonow from firebase
})

const handeleChange= e =>{
    setFormData({...formData, [e.target.name]: e.target.value})
}
const handeleImagenChange= e =>{
    setFormData({...formData, image: e.target.files[0] })
}

const [progres, setProgres] = useState(0)
const handlePublish = (e)=>{
    console.log(formData)
    if(!formData.name ||!formData.description ||!formData.image) {// see empty
        alert("empty field")
        }

    // create dir firebase to upload all files images
    const storageRef = ref(storage, `images/${Date.now()}${formData.image.name}`) 
    const uploadImage = uploadBytesResumable(storageRef, formData.image)
    // Progres Percent Upload
    uploadImage.on("state_changed", (snapshot)=>{
        const progressPercent = Math.round((snapshot.bytesTransferred / snapshot.totalBytes)*100)
        setProgres(progressPercent)
        },
        (err)=> {

            console.log(err);
        },
        ()=>{
            setFormData({
                name:"",
                description: "",
                image: "",
                
            });
            getDownloadURL(uploadImage.snapshot.ref)
            .then((url)=>{
                const skillRef = collection(db, "Skills");
                addDoc(skillRef, {
                    name: formData.name,
                    description: formData.description,
                    image: url, 
                    createdAt : Timestamp.now().toDate() // funtion format date autonow from firebase
                })
                .then(()=>{
                    alert("Skill add successfully", {type: "success"});
                    setProgres(0)
                })
                .catch(err=>{
                    alert("Error", {type: "error"});
                    
                })
            })
        }
    )
    e.preventDefault();
    e.target.reset();
}
```

```html
<form action="">
<div>
    <label htmlFor="name"> name</label>
    <input onChange={(e)=>handeleChange(e)} value={formData.name} type="text" name='name'  />
</div>
<div>
    <label htmlFor="description"> description</label>
    <textarea onChange={(e)=>handeleChange(e)} value={formData.description} name="description" id="" cols="30" rows="2"></textarea>
</div>
{/* imagen to public */}
<div>
    <label htmlFor="image" className='h-1'> image</label>
    <input onChange={(e)=>handeleImagenChange(e)} type="file" accept='images/skills' name='image' />
</div>
{progres==!0 &&

<div className="w-full bg-gray-200 rounded-full">
    <div className="bg-blue-600 text-xs font-medium text-blue-100 text-center p-05 leading-none rounded-l-full" 
    style={{width: "{progres}%"}}> 
    {progres}%</div>
</div>
}

<div>
    <button onClick={(e)=>handlePublish(e)} className='bg-gray-600 hover:text-gray-800 px-3 pb-1 rounded-xl'>submit</button>
</div>

</form>
```