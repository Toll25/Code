//pfeilfunktionen

// Array mit Zahlen

const list = [1, 2, 3];

// Anforderung: erstelle list mi den doppelten ursprünglichen werten

// const doubleMyNumber = (number) => { return number * 2 };
const doubleMyNumber = (number) => number * 2;

const doubledList = list.map(doubleMyNumber);

console.log(list);

console.log(doubledList);