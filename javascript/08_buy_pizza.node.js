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

function ask_even_number(question_string, prev_answers = []) {
  function f(x) {
    num = Number(x);
    return !isNaN(num) && (num > 0) && (num % 2 == 0)
  }
  return ask_condition(question_string, f, prev_answers)
}

function calc_pizza_leftover(n_piece, n_people) {
  per_person = Math.floor(n_piece / n_people)
  leftover = n_piece - per_person * n_people 

  return {per_person: per_person, leftover: leftover}
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


ask_number('How many people? ')
  .then(([n_people, _]) => { return ask_even_number('How many pieces in a pizza? ', [n_people]) })
  .then(([n_piece, [n_people]]) => { return ask_even_number('How many pieces per person? ', [n_people, n_piece]); })
  .then(([n_piece, [n_people, per_person]]) => { 
    n_pizza = Math.ceil(n_people * per_person / n_piece)
    total_piece = n_pizza * n_piece

    resp = calc_pizza_leftover(total_piece, n_people)
    per_person = resp.per_person;
    leftover = resp.leftover;

    console.log(`${n_people} ${match_number('person', n_people)} with ${n_pizza} ${match_number('pizza', n_pizza)}.`)
    console.log(`Each person gets ${per_person} ${match_number('piece', per_person)} of pizza.`)
    console.log(`There are ${leftover} leftover ${match_number('piece', leftover)}.`)
    rl.close();
  });
