#!/usr/bin/node
const args = process.argv.slice(2);
const number = Number(args[0]);
let str = '';
if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    for (let j = 0; j < number; j++) {
      str = str.concat('X');
    }
    str = str.concat('\n');
  }
  str = str.slice(0, -1);
  console.log(str);
}
