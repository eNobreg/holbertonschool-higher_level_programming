#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

const url = args[0];
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  let total = 0;
  const json = JSON.parse(body).results;
  for (const entry of json) {
    for (const charUrl of entry.characters) {
      if (charUrl.includes('18')) {
        total++;
      }
    }
  }
  console.log(total);
});
