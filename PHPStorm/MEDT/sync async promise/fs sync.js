import{readFileSync} from 'node:fs'

console.log('A')

const fileContent = readFileSync('./input.txt', 'utf8')

console.log('B')

console.log(fileContent)

console.log('C')