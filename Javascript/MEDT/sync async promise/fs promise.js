import{readFile} from 'node:fs/promises'

console.log('A')

const promise = readFile('./input.txt', 'utf8')

promise.then((data => {
    console.log('B')
    console.log(data)
})).catch((error) => {
    console.error(error.message)
})

console.log('C')