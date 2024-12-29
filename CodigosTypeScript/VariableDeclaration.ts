//Created Date: 31/07/2022
//Last Update: 28/12/2024
//Description: Just some use case for TypeScript
//Observation: Some forms of use to train
var message : string = "Hello World!"
console.log(message)

// Different ways of Variable Declaration
/*------------------------------------------------------*/
var a : number // Apenas Datatype
var b = 10 // Datatype e opcional. Apenas inicializacao
var c : number = 10 // Ambos
var d // Nenhum dos 2

// var consegue ser redeclarado mas tem que ser para o mesmo tipo
console.log(b)
b = 15
console.log(b)

var b : number = 100
console.log(b)

// Atribuir um valor e com o =
let l // Nao e obrigatorio iniciar
let testLet : string // Datatype declarado

// let consegue ser alterado mas nao consegue ser redeclarado
let newTestLet : string = "Hello"
console.log(newTestLet)
newTestLet = "World"
console.log(newTestLet)

// const nao consegue ser redeclarado ou alterado
const con : number = 1 // const tem que ser iniciado

// function
// Variaveis criadas dentro de um bloco como IF nao serao reconhecidas fora dele
function exemple(){
    if (true){
        var x = 100
        console.log(x)
    }
}