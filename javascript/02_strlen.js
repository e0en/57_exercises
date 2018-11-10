const question_str = 'What is the input string?'

function length_message(input_str) {
  if (input_str.length > 0) {
    return `${input_str} has ${input_str.length} characters.`;
  } else {
    return 'Please input a non-empty string.';
  }
}

document.addEventListener('DOMContentLoaded', function() {
  var form = document.createElement('form');
  form.setAttribute('action', '#');

  var label = document.createElement('label');
  label.setAttribute('for', 'input_string');
  label.innerText = question_str;

  var input = document.createElement('input');
  input.setAttribute('type', 'text');
  input.setAttribute('name', 'input_string');

  var submit = document.createElement('input');
  submit.setAttribute('type', 'submit');

  var message = document.createElement('p');

  form.appendChild(label);
  form.appendChild(input);
  form.appendChild(document.createElement('br'));
  form.appendChild(submit);

  document.body.appendChild(form);
  document.body.appendChild(message);

  input.onkeyup = function(e) {
    input_string = input.value;
    message.innerText = length_message(input_string);
    return false;
  };

}, false);
