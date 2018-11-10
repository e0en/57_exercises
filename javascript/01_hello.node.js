const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function greet(name) {
  console.log(`Hello ${name}, nice to meet you!`)
  rl.close()
}


rl.question('What is your name? ', greet)
