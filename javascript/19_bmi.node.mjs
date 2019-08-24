import { rl, ask, ask_number } from './xx_ask.mjs'

const msg = `Your height in inches: `

function bmi(h, w) {
  return (w / (h * h)) * 703;
}

ask(msg)
  .then(([height_str, _]) => { 
    const ask_weight_msg = `Your weight in pounds: `
    return ask(ask_weight_msg, [height_str])
  })
  .then(([weight_str, [height_str]]) => {
    const height = Number(height_str)
    const weight = Number(weight_str)
    const result = bmi(height, weight)

    console.log(`Your BMI is ${result}.`)
    if (result < 18.5) {
      console.log(`You are underweight. You should see your doctor.`)
    } else if (result > 25) {
      console.log(`You are overweight. You should see your doctor.`)
    } else {
      console.log(`You are within ideal weight range.`)
    }
    rl.close();
  });
