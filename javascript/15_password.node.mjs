import * as readline from 'readline'
import { Writable } from 'stream'

var mutableStdout = new Writable({
  write: function(chunk, encoding, callback) {
    if (!this.muted) {
      process.stdout.write(chunk, encoding);
    }
    callback();
  }
})

mutableStdout.muted = false

const rl = readline.createInterface({
    input: process.stdin,
    output: mutableStdout,
    terminal: true
});


const stored_pw = 'abc$123'

rl.question('What is the password? ', function(pw) {
  console.log('')
  if (pw === stored_pw) {
    console.log('Welcome!')
  } else {
    console.log('That password is incorrect.')
  }
  rl.close();
})

mutableStdout.muted = true
