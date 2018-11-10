const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function answer(input_string) {
  if (input_string.length > 0) {
    console.log(`${input_string} has ${input_string.length} characters.`)
  } else {
    console.log('Please input a non-empty string.')
  }
  rl.close()
}


rl.question('What is the input string? ', answer)
