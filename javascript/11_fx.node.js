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

function match_number(noun, n) {
  if (n == 1) {
    result = noun
  } else if (noun == 'person') {
    result = 'people'
  } else {
    result = noun + 's'
  }
  return result
}

ask_number('How many Euros are you exchanging? ')
  .then(([euros, _]) => { return ask_number('What is the exchange rate? ', [euros]) })
  .then(([rate_from_eur, [euros]]) => { 
    dollars = Math.ceil(euros * rate_from_eur) / 100.0
    console.log(`${euros} Euros at exchange rate3 ${rate_from_eur} is ${dollars.toFixed(2)} dollars`)
    rl.close();
  });
