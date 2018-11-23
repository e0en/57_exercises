const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


function ask(question_string, prev_answers = []) {
  return new Promise((resolve) => rl.question(question_string, (input) => resolve([input, prev_answers])));
}

function ask_number(question_string, prev_answers = []) {
  return ask(question_string, prev_answers).then(([input, prev]) => {
    num = Number(input);
    if (isNaN(num) || num < 0) {
      console.log('You must input a non-negative number');
      return ask_number(question_string, prev_answers);
    } else {
      return new Promise((resolve) => resolve([num, prev_answers]));
    }
  });
}

ask_number('What is your age? ')
  .then(([age, _]) => { return ask_number('At what age would you like to retire? ', [age]); })
  .then(([retire_age, [age]]) => { 
    if (retire_age <= age) {
      console.log('You should have been retired already.')
    } else {
      const today = new Date();
      const year = today.getFullYear();
      console.log(`You have ${retire_age - age} years left until you can retire.
It's ${year}, so yo can retire in ${year + retire_age - age}.`);
    }
    rl.close();
  });
