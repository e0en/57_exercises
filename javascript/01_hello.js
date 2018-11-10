const question_str = 'What is your name? '

function greet(name) {
  return `Hello ${name}, nice to meet you!`;
}

document.addEventListener('DOMContentLoaded', function() {
  var form = document.createElement('form');
  form.setAttribute('action', '#');

  var label = document.createElement('label');
  label.setAttribute('for', 'name');
  label.innerText = question_str;

  var input = document.createElement('input');
  input.setAttribute('type', 'text');
  input.setAttribute('name', 'name');

  var submit = document.createElement('input');
  submit.setAttribute('type', 'submit');

  var answer = document.createElement('p');

  form.appendChild(label);
  form.appendChild(input);
  form.appendChild(document.createElement('br'));
  form.appendChild(submit);

  document.body.appendChild(form);
  document.body.appendChild(answer);

  form.onsubmit = function(e) {
    name = input.value;
    answer.innerText = greet(name);
    return false;
  };

}, false);
