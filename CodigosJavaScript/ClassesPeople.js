/*
Created Date: 14/01/2024
Last Update: 30/11/2024
Description: Test creating class in JavaScript
Observation: Creating a class in JavaScript and showing everything in the console
*/

console.log('Testing creating classes using JS.');

class People {
    name;
    weight;
    hight;

    constructor (name, weight, hight) {
        this.name = name;
        this.weight = weight;
        this.hight = hight;
    }

    imcCalculation() {
        return this.weight / Math.pow(this.hight, 2);
    }

    imcClassification() {
        const imcValue = this.imcCalculation();
        let message = '';
        if (imcValue < 18.5) {
            message = 'Under the ideal weight';
        } else if (imcValue >= 18.5 && imcValue < 25) {
            message = 'Normal weight';
        } else if (imcValue >= 25 && imcValue < 30) {
            message = 'Above the ideal weight';
        } else if (imcValue >= 30 && imcValue < 40) {
            message = 'Obesity';
        } else {
            message = 'Severe Obesity';
        }
        return message;
    }
}

const person1 = new People('Person 1', 83, 1.73);

console.log(person1.imcCalculation());