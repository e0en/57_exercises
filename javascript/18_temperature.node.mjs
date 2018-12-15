import { rl, ask, ask_number } from './xx_ask.mjs'

const msg = `Press C to convert from Fahrenheit to Celcius.
Press F to convert from Celcius to Fahrenheit.
Your choice: `

function celcius_to_fahrenheit(c) {
  return c * 9 / 5 + 32
}

function fahrenheit_to_celcius(f) {
  return (f - 32) * 5 / 9
}

ask(msg)
  .then(([ch, _]) => { 
    const from_unit = ch == 'C' ? 'Fahrenheit' : 'Celcius'
    const ask_num_msg = `Please enter the temperature in ${from_unit}: `
    return ask(ask_num_msg, [ch])
  })
  .then(([temp_str, [ch]]) => {
    const to_unit = ch == 'C' ? 'Celcius' : 'Fahrenheit'
    const from_temp = Number(temp_str)

    const to_temp = (ch == 'C') ? fahrenheit_to_celcius(from_temp) : celcius_to_fahrenheit(from_temp)
    console.log(`The temperature in ${to_unit} is ${to_temp}.`)
    rl.close();
  });
