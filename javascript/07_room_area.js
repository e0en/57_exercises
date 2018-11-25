function calc_area(len, width) {
  return len * width
}

document.addEventListener('DOMContentLoaded', function() {
  var form = document.createElement('form')
  form.setAttribute('action', '#')

  var label_meter = document.createElement('label')
  label_meter.setAttribute('for', 'meters')
  label_meter.innerText = 'meters '

  var input_meter = document.createElement('input')
  input_meter.setAttribute('type', 'radio')
  input_meter.setAttribute('name', 'unit')
  input_meter.value = 'meters'

  var label_feet = document.createElement('label')
  label_feet.setAttribute('for', 'feet')
  label_feet.innerText = 'feet '

  var input_feet = document.createElement('input')
  input_feet.setAttribute('type', 'radio')
  input_feet.setAttribute('name', 'unit')
  input_feet.value = 'feet'

  var label_length = document.createElement('label')
  label_length.setAttribute('for', 'length')
  label_length.innerText = 'What is the length of the room in ? '

  var input_length = document.createElement('input')
  input_length.setAttribute('type', 'number')
  input_length.setAttribute('name', 'length')


  var label_width = document.createElement('label')
  label_width.setAttribute('for', 'width')
  label_width.innerText = 'What is the width of the room in ? '

  var input_width = document.createElement('input')
  input_width.setAttribute('type', 'number')
  input_width.setAttribute('name', 'width')

  var submit = document.createElement('input')
  submit.setAttribute('type', 'submit')

  var answer = document.createElement('p')

  form.appendChild(label_meter)
  form.appendChild(input_meter)
  form.appendChild(label_feet)
  form.appendChild(input_feet)
  form.appendChild(document.createElement('br'))
  form.appendChild(label_length)
  form.appendChild(input_length)
  form.appendChild(document.createElement('br'))
  form.appendChild(label_width)
  form.appendChild(input_width)
  form.appendChild(document.createElement('br'))
  form.appendChild(submit)

  document.body.appendChild(form)
  document.body.appendChild(answer)

  sq_feet_in_meters = 0.09290304

  function onchange(e) {
    if (input_meter.checked) {
      unit = 'meters'
      alt_unit = 'feet'
    } else {
      unit = 'feet'
      alt_unit = 'meters'
    }

    len = Number(input_length.value)
    width = Number(input_width.value)
    if (isNaN(len) || isNaN(width)) {
      answer.innerText = 'Please input a number'
    } else {
      area = calc_area(len, width)
      if (unit == 'feet') {
        alt_area = area * sq_feet_in_meters
      } else if (unit == 'meters') {
        alt_area = area / sq_feet_in_meters
      }
      answer.innerText = `You entered dimensions of ${len} ${unit} by ${width} ${unit}. \n`
      answer.innerText += `The area is \n`
      answer.innerText += `${area} square ${unit}. \n`
      answer.innerText += `${alt_area} square ${alt_unit}. \n`
    }
    return false
  }

  form.onsubmit = onchange
  input_meter.onchange = onchange
  input_feet.onchange = onchange
  input_length.onkeyup = onchange
  input_width.onkeyup = onchange
  onchange()
}, false)
