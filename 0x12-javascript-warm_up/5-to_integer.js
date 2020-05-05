#!/usr/bin/node
const args = process.argv.slice(2);
const convert = Number(args[0]);
if (isNaN(convert)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + convert);
}
