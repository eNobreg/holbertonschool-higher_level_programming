#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);

const url = args[0];
request(url, function (err, resp, body) {
  const userDict = {};
  if (err) {
    console.log(err);
  }
  const json = JSON.parse(body);
  for (const entry of json) {
    if (entry.completed === true) {
      if (userDict[entry.userId]) {
        userDict[entry.userId] += 1;
      } else {
        userDict[entry.userId] = 1;
      }
    }
  }
  console.log(userDict);
});
