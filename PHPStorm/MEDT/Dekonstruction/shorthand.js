const address = {
    firstName: 'Eduard',
    lastName: 'Müller',
    street: 'Anton Ehrenfried-Straße',
    houseNr: 10,
    zipCode: 2020,
    city: 'Hollabrunn'
};

console.log(address)

const {firstName, lastName,street,houseNr,zipCode,city} = address;
console.log(firstName)
console.log(lastName)

const address2 = {
    firstName: firstName,
    lastName: lastName,
    street: street,
    houseNr: houseNr,
    zipCode: zipCode,
    city: city
};

console.log(address2)

const address3 = {
    firstName,
    lastName,
    street,
    houseNr,
    zipCode,
    city
}

console.log(address3)
