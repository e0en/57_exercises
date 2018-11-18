function show_calculations(num1, num2) {
  return `${num1} + ${num2} = ${num1 + num2}
${num1} - ${num2} = ${num1 - num2}
${num1} * ${num2} = ${num1 * num2}
${num1} / ${num2} = ${num1 / num2}`;
}

document.addEventListener('DOMContentLoaded', function() {
  var form = document.createElement('form');
  form.setAttribute('action', '#');

  var label1 = document.createElement('label');
  label1.setAttribute('for', 'number1');
  label1.innerText = 'What is the first number?';

  var input1 = document.createElement('input');
  input1.setAttribute('type', 'number');
  input1.setAttribute('name', 'number1');


  var label2 = document.createElement('label');
  label2.setAttribute('for', 'number2');
  label2.innerText = 'What is the second number?';

  var input2 = document.createElement('input');
  input2.setAttribute('type', 'number');
  input2.setAttribute('name', 'number2');

  var submit = document.createElement('input');
  submit.setAttribute('type', 'submit');

  var answer = document.createElement('p');

  form.appendChild(label1);
  form.appendChild(input1);
  form.appendChild(document.createElement('br'));
  form.appendChild(label2);
  form.appendChild(input2);
  form.appendChild(document.createElement('br'));
  form.appendChild(submit);

  document.body.appendChild(form);
  document.body.appendChild(answer);

  function onchange(e) {
    num1 = Number(input1.value);
    num2 = Number(input2.value);
    if (isNaN(num1) || isNaN(num2)) {
      answer.innerText = 'Please input a number';
    } else {
      answer.innerText = show_calculations(num1, num2);
    }
    return false;
  };

  form.onsubmit = onchange;
  input1.onkeyup = onchange;
  input2.onkeyup = onchange;
  onchange();
}, false);
