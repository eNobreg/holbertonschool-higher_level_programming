#!/usr/bin/node
const array = require('./100-data.js').list;
const newArray = array.map((x, i) => x * i);
console.log(array);
console.log(newArray);
