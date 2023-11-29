const person = {
    firstName: 'Eduard',
    lastName: 'Müller',
    getFullName: () => {
        const name = `${this.firstName} ${this.lastName}`
        console.log(this)
        return name
    }
}

//console.log(person.getFullName())

class Person {
    constructor(firstName,lastName) {
        console.log("Constructor!!!")
        this.firstName=firstName;
        this.lastName=lastName;
    }
}
const p = new Person('Eduard','Müller')
console.log(p)
console.log({})