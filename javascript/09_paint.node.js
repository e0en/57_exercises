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


ask_number('Width of your room in meters? ')
  .then(([width, _]) => { return ask_number('Length of your room in meters? ', [width]) })
  .then(([len, [width]]) => {
    liter_per_sqmeter = 9
    area = width * len
    paint_liters = Math.ceil(area / liter_per_sqmeter)
    console.log(`You will need to purchase ${paint_liters} liters of paint to cover ${area} square meters.`)
    rl.close();
  });
