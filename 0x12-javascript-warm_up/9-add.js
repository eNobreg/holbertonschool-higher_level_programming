#!/usr/bin/node
function add(a, b) {
    return (Number(a) + Number(b));
}
const args = process.argv.slice(2);
console.log(add(args[0], args[1]));
