#!/usr/bin/node
function factorial (number) {
  if (number <= 0) {
    return 1;
  } else {
    return (number * factorial(number - 1));
  }
}
const args = process.argv.slice(2);
const num = Number(args[0]);
if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(num));
}
