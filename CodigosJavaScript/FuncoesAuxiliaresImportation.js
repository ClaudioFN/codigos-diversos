
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