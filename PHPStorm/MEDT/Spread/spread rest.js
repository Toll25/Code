const contact = {
    firstName: 'Eduard',
    lastName: 'Müller',
    email: 'eduard.mueller@gmail.com',
    phone: "+43034204230",
};

const {email, ...rest} = contact;
console.log(email)
console.log(rest)

function printNumbers(...list){
    list.forEach(x=> console.log(x))
}
printNumbers(1,2,3,4,5)
printNumbers()

function printAttributes({...rest}){
    console.log(rest)
}

printAttributes({name:`Hugo`, age: 123})