// Boolean
let turnedON: boolean = false;
// String
let nome: string = "Nome";
// Number
let age: number = 30;
// Number with decimal
let hight: number = 1.4;

/// Special Types
// Null
let nulo: null = null;
// Undefined
let undefinedVariable: undefined = undefined;

// Another Types
// Any | void
let returnVariableVoid: void;
let returnVariableAny: any = false;
// -----------------------------------------------------------
// Objects - not predictable
let product: object = {
    name: "Car",
    city: "SP",
    age: 10
};

// Typed object - predictable
type StoreProduct = {
    name: string;
    price: number;
    unities: number;
};

let myProduct: StoreProduct = {
    name: "Shoes",
    price: 109.99,
    unities: 1
};
// -----------------------------------------------------------
// Arrays
let data: string[] = ["Jurema", "Rogério", "Pato"];
let data2: Array<string> = ["Jurema", "Rogério", "Pato"];
// -----------------------------------------------------------
// Multiples types Arrays
let infos: (string | number)[] = ["Jurema", 20, 10, "Alecrim"];
// -----------------------------------------------------------
// Tuplas
let valueToPay: [string, number, number] = ["Conta", 100, 150];
// -----------------------------------------------------------
// Dates
let birthDate: Date = new Date("01-01-2000 05:08");
console.log(birthDate.toString());
// -----------------------------------------------------------
// Functions
function addNumber(x: number, y: number): number {
    return x + y;
}
let soma: number = addNumber(5, 10);
// -----------------------------------------------------------
// Functions With Multiples Types
function callToPhone(phone: number | string) {
    return phone;
}
callToPhone("1122334455667788");
callToPhone(1122334455667788);
// -----------------------------------------------------------
// Async Functions
async function getDatabase(id:number): Promise<string> {
    return "NAME";
}
// -----------------------------------------------------------
// Classes
class Character {
    name: string;
    strength: number;
    skill: number;

    constructor(name: string, strength: number, skill: number){
        this.name = name;
        this.strength = strength;
        this.skill = skill;
    }

    attack(): void {
        console.log(`${this.name} attacks with ${this.strength} points!`);
    }
}

const p1 = new Character('Batman', 10, 98);
p1.attack();
// -----------------------------------------------------------
// Modifiers
// public: todos conseguem enxergar
// private: acessado apenas dentro da classe.
// protected: usado dentro da classe e classes que herdam
// -----------------------------------------------------------
// Generics -> T
//function concatArray(...items: any[]): any[] {
//    return new Array().concat(...items);
//}

function concatArray<T>(...items: T[]): T[] {
    return new Array().concat(...items);
}

const numArray = concatArray<number[]>([1, 5], [3]);
const stgArray = concatArray<string[]>(['Rail', 'Gun'], ['Tox']);
console.log(numArray);
console.log(stgArray);
// -----------------------------------------------------------
// Decorators - decore uma funcao para disparar outra acao
function showName(target: any) {
    console.log(target);
}

@showName
class employer{}

@showName
class bread {}
//---
function apiVersion(version: string) {
    return (target: any) => {
        Object.assign(target.prototype, { __version: version});
    };
}

@apiVersion("1.10")
class Api {}

const api = new Api();
// console.log(api.__version); - injetando a propriedade inexistente na classe
// -----------------------------------------------------------

// -----------------------------------------------------------
