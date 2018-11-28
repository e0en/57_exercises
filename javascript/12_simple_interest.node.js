const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


function ask(question_string, prev_answers = []) {
  return new Promise((resolve) => rl.question(question_string, (input) => resolve([input, prev_answers])));
}


function ask_condition(question_string, f, prev_answers = []) {
  return ask(question_string, prev_answers).then(([input, prev]) => {
    if (!f(input)) {
      console.log('Input is invalid');
      return ask_condition(question_string, f, prev_answers);
    } else {
      return new Promise((resolve) => resolve([input, prev_answers]));
    }
  });
}

function ask_number(question_string, prev_answers = []) {
  function f(x) {
    num = Number(x);
    return !(isNaN(num) || num < 0)
  }
  return ask_condition(question_string, f, prev_answers)
}

ask_number('Enter the principal: ')
  .then(([principal, _]) => { return ask_number('Enter the rate of interest: ', [principal]) })
  .then(([rate, l]) => { return ask_number('Enter the number of years: ', l.concat([rate])) })
  .then(([years, [principal, rate]]) => { 
    worth = principal * (1 + rate * years / 100.0)
    worth = Math.ceil(worth * 100.0) / 100.0

    worth = worth.toFixed(2)
    console.log(`After ${years} years at ${rate}%, the investment will be worth \$${worth}`)
    rl.close();
  });
