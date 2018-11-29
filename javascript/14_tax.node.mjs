import { rl, ask, ask_number } from './xx_ask.mjs'

ask_number('What is the order amount? ')
  .then(([order, _]) => { return ask('What is the state? ', [order]) })
  .then(([state, [order]]) => {
    const subtotal = Number(order)
    let total = subtotal
    if (state.toLowerCase() == 'wi') {
      const tax = Math.round(subtotal * 0.055 * 100) / 100.0
      total += tax
      console.log(`The subtotal is \$${subtotal}`)
      console.log(`The tax is \$${tax}`)
    }
    console.log(`The total is \$${total}`)
    rl.close();
  });
