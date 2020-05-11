#!/usr/bin/node
const fs = require('fs');
const args = process.argv.slice(2);

const string = fs.readFileSync(args[0]).toString();
const string2 = fs.readFileSync(args[1]).toString();
const string3 = string.concat(string2);
fs.writeFile(args[2], string3, function (err) {
  if (err) {
    return console.error(err);
  }
});
