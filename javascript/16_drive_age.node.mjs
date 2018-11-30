import { rl, ask, ask_number } from './xx_ask.mjs'

ask_number('What is your age? ')
  .then(([age_str, _]) => {
    const age = Number(age_str)
    const enough = age >= 16 ? 'old enough' : 'not old enough'
    console.log(`You are ${enough} to legally drive.`)
    rl.close();
  });
