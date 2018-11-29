import * as readline from 'readline'

export const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


export function ask(question_string, prev_answers = []) {
  return new Promise((resolve) => {
    rl.question(question_string, (input) => resolve([input, prev_answers]))
  });
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

export function ask_number(question_string, prev_answers = []) {
  function f(x) {
    const num = Number(x);
    return !(isNaN(num) || num < 0)
  }
  return ask_condition(question_string, f, prev_answers)
}

function ask_even_number(question_string, prev_answers = []) {
  function f(x) {
    const num = Number(x);
    return !isNaN(num) && (num > 0) && (num % 2 == 0)
  }
  return ask_condition(question_string, f, prev_answers)
}

export function match_number(noun, n) {
  if (n == 1) {
    return noun
  } else if (noun == 'person') {
    return 'people'
  } else {
    return noun + 's'
  }
}
