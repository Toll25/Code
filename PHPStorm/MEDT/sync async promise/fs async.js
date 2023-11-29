import{readFile} from 'node:fs'

console.log('A')

const fileContent = readFile('./input.txt', 'utf8', (error, data) =>  {
    if(error!=null){
        console.error(error.message)
    }else{
        console.log('B')
        console.log(data)
    }

})

console.log(fileContent)

console.log('C')