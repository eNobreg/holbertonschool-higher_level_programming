#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const args = process.argv.slice(2);

const options = {
  url: args[0],
  method: 'GET'
};

request(options, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(args[1], body, 'utf-8', function (err, data) {
      if (err) {
        console.log(err);
      }
    });
  }
});
