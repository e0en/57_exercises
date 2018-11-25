const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


function ask(question_string, prev_answers = []) {
  return new Promise((resolve) => rl.question(question_string, (input) => resolve([input, prev_answers])));
}


function ask_choice(question_string, choices, prev_answers = []) {
  return ask(question_string, prev_answers).then(([input, prev]) => {
    if (isNaN(num) || num < 0) {
      console.log('You must input a non-negative number');
      return ask_number(question_string, prev_answers);
    } else {
      return new Promise((resolve) => resolve([num, prev_answers]));
    }
  });
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

ask('Choose your length unit (meters/feet) ')
  .then(([unit, _]) => { return ask_number(`What is the length of the room in ${unit}? `, [unit]) })
  .then(([room_length, [unit]]) => { return ask_number(`What is the width of the room in ${unit}? `, [unit, room_length]); })
  .then(([room_width, [unit, room_length]]) => { 
    const area = room_length * room_width

    console.log(`The entered dimensions of ${room_length} feet by ${room_width} ${unit}`)
    console.log('The area is')

    if (unit == 'feet') {
      console.log(`${area} square feet`)
      console.log(`${area * 0.09290304} square meters`)
    } else if (unit == 'meters') {
      console.log(`${area} square meters`)
      console.log(`${area / 0.09290304} square feets`)
    }
    rl.close();
  });
