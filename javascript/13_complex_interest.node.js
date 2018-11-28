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

ask_number('What is the principal amount? ')
  .then(([principal, _]) => { return ask_number('What is the rate? ', [principal]) })
  .then(([rate, l]) => { return ask_number('What is the number of years: ', l.concat([rate])) })
  .then(([years, l]) => { return ask_number('What is the number of times the interest is compounded per year: ', l.concat([years])) })
  .then(([compound_freq, [principal, rate, years]]) => { 
    worth = principal * Math.pow(1 + rate / 100.0 / compound_freq, compound_freq * years)
    worth = Math.ceil(worth * 100.0) / 100.0

    worth = worth.toFixed(2)
    console.log(`\$${principal} invested at ${rate}% for ${years} years compounded ${compound_freq} times per year is \$${worth}`)
    rl.close();
  });
