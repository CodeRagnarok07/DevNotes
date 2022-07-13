// importa demaciado la asignacion de datos

var myString: string = "hola mundo"
var myNumber = 2
var myBool: boolean = true || false

// array
var myArryOfString: Array<string> = ["2", "1"]
var myArryOfNumber: Array<number> = [2, 1]
var myArryOfarrya: Array<any> = [myArryOfNumber, myArryOfString]
var arryOfAll: any[] = [myArryOfNumber, myArryOfString, myArryOfarrya, myBool, myNumber, myString]

// Tuple son estructuras definidas
var myTuple: [string, number] = ["hola", 545];


// fetch("https://public-api.wordpress.com/wp/v2/sites/angelriera.wordpress.com/")
// .then(res=> console.log(res.json()) )
// .then(res=> console.log(res))

// funtions

//asigna las variable numero o string y lo que retorna

function get3sum(n1: number, n2: number, n3?): number | string {
    return `${n1}+${n2}+${n3}`
}
get3sum(5, 9)

// INTERFACES

interface newObj { name: string, title: string, date: number }

const getObj = (objeto: newObj) => {
    return console.log(`${objeto.title} ${objeto.name}}`);
}
var datos: newObj = { name: "angel", date: 546, title: "sads" }

// getObj(datos)


// class

class Pokemon {
    name: string;
    private element: string;
    public hp: number;
    protected sp: number;
    str: number;


    constructor(name: string, element: string, hp: number, sp: number, str: number) {
        this.name = name;
        this.element = element;
        this.hp = hp;
        this.sp = sp;
        this.str = str;
    }
    pokedex() {
        return console.log(`name:${this.name}:: Elemento:${this.element}:: HP${this.hp}:: SP${this.sp}:: STR${this.str} ::`)
    }
}

// herencia de clases
var charmander = new Pokemon("charmander", "tierruo", 65, 65, 78)
charmander.pokedex()
class digimon extends Pokemon {
    evolucion: string;
    constructor(evolucion: string, name, element, hp, sp, str) {
        super(name, element, hp, sp, str) // erencia de pokemons
        this.name = name
    }
    pokedex(): void {
        super.pokedex()
    }

}



document.write(arryOfAll.toString())


export { } // evita los errores de funciones

// $ tsc file.ts // => compila y crea un file.js
