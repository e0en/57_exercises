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

ask('Enter a noun: ')
  .then(([noun, _]) => { return ask('Enter a verb: ', [noun]); })
  .then(([verb, [noun]]) => { return ask('Enter an adjective: ', [noun, verb]); })
  .then(([adjective, [noun, verb]]) => { return ask('Enter an adverb: ', [noun, verb, adjective]); })
  .then(([adverb, [noun, verb, adjective]]) => { 
    console.log(`Do you ${verb} your ${adjective} ${noun} ${adverb}? That's hilarious!`);
    rl.close(); 
  });
