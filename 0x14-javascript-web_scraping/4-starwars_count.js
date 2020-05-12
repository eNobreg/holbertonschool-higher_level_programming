#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);


const url = args[0];
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let total = 0;
    const json = JSON.parse(body).results;
    for (const entry of json) {
      if (entry.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        total += 1;
      }
    }
    console.log(total);
  }
});
