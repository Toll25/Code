const firstName = 'Eduard';
const lastName = 'Müller';
const street = 'Anton Ehrenfried-Straße';
const houseNr = 10;
const zipCode = 2020;
const city = 'Hollabrunn';

// Template Strings mit interpolation

// Template -> Vorlage / Schablone
// -> innerhalb von ${} kann javascript code stehen

const address = `${firstName} ${lastName}
${street} ${houseNr}
${zipCode} ${city}`;

console.log(address);