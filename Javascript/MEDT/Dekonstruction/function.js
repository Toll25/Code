const address = {
    firstName: 'Eduard',
    lastName: 'Müller',
    street: 'Anton Ehrenfried-Straße',
    houseNr: 10,
    zipCode: 2020,
    city: 'Hollabrunn'
};

function printAddress({firstName, lastName, city, country="Österreich"}) {
    console.log(`${firstName} ${lastName} - ${city} ${country}`)
}

printAddress(address)