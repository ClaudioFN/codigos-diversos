/*
Created Date: 21/01/2024
Last Update: 02/03/2025
Description: Help functions
Observation: Just a way to use some functions to support the others classes
*/
const entrances = [5, 10, 15, 20, 25];

let i = 0;

function gets() {
    const value = entrances[i];
    i++;
    return value;
}

function print(text) {
    console.log(text);
}

module.exports = { gets, print };