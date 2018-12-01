import { rl, ask, ask_number } from './xx_ask.mjs'

ask_number('How much alcohol did you drink in oz? ')
  .then(([oz_str, _]) => { return ask_number('Your weight in lb? ', [oz_str]) })
  .then(([lb_str, l]) => { return ask('Your gender (m/f)? ', l.concat([lb_str])) })
  .then(([gender, l]) => { return ask_number('Hours after your last drink? ', l.concat([gender])) })
  .then(([hr_str, [oz_str, lb_str, gender]]) => {
    const oz = Number(oz_str)
    const lb = Number(lb_str)
    const hours = Number(hr_str)
    const coeff = gender === 'm' ? 0.73 : 0.60
    const bac = (oz * 5.14 / lb * coeff) - 0.15 * hours
    const is_legal_str = bac > 0.08 ? 'not legal' : 'legal'
    console.log(`Your BAC is ${bac}`)
    console.log(`It is ${is_legal_str} for you to drive.`)
    rl.close();
  });
