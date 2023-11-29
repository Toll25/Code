const address = {
    firstName: 'Eduard',
    lastName: 'Müller',
    street: 'Anton Ehrenfried-Straße',
    houseNr: 10,
    zipCode: 2020,
    city: 'Hollabrunn'
};
const contact = {
    firstName: 'Eduard',
    lastName: 'Müller',
    email: 'eduard.mueller@gmail.com',
    phone: "+43034204230",
};

const person = Object.assign(address,contact)
//console.log(person)

const person2 = Object.assign({}, address,contact)
//console.log(person2)

