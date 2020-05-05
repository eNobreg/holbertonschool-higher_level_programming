#!/usr/bin/node
let args = process.argv.slice(2);
const len = args.length;
if (args.length === 0) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  args = args.sort(function (a, b) { return a - b; });
  console.log(args[len - 2]);
}
