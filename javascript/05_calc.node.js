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

ask_number('What is the first number? ')
  .then(([num1, _]) => { return ask_number('What is the second number? ', [num1]); })
  .then(([num2, [num1]]) => { 
    console.log(`${num1} + ${num2} = ${num1 + num2}
${num1} - ${num2} = ${num1 - num2}
${num1} * ${num2} = ${num1 * num2}
${num1} / ${num2} = ${num1 / num2}`);
    rl.close();
  });
