const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function ask(question_string, prev_answers = []) {
  return new Promise((resolve) => {
    rl.question(question_string, (input) => resolve([input, prev_answers]));
  });
}

ask('What is the quote? ')
  .then(([quote, _]) => { return ask('Who said it? ', [quote]); })
  .then(([whom, [quote]]) => { 
    console.log(whom + ' says, "' + quote + '."'); 
    rl.close(); 
  });
