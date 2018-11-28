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

function ask_cachier_item(item_name, prev_answers = []) {
  return ask_number(`Price of ${item_name}: `)
    .then(([price, _]) => { return ask_number(`Quantity of ${item_name}: `, [price]) })
    .then(([qty, [price]]) => { 
      item_info = {price: price, quantity: qty}
      return new Promise((resolve) => resolve([item_info, prev_answers]));
    });
}

tax_rate = 0.055

ask_cachier_item('item 1')
  .then(([item1, _]) => { return ask_cachier_item('item 2', [item1]) })
  .then(([item2, l]) => { return ask_cachier_item('item 3', l.concat([item2])) })
  .then(([item3, l]) => {
    l = l.concat([item3])
    subtotal = 0.0
    l.forEach((i) => subtotal += i.price * i.quantity)
    console.log(`Subtotal: \$${subtotal.toFixed(2)}`)
    tax = subtotal * tax_rate
    console.log(`Tax: \$${tax.toFixed(2)}`)
    total = (subtotal + tax).toFixed(2)
    console.log(`Total: \$${total}`)
    rl.close();
  });
