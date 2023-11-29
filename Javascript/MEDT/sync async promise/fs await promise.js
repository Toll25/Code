import{readFile} from 'node:fs/promises'

console.log('A')

try{
    const data = await readFile('./input.txt', 'utf8')
    console.log('B')
    console.log(data)
}catch (error){
    console.error(error.message)

}

console.log('C')