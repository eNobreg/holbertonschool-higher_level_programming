#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);

const options = {
  url: args[0],
  method: 'GET'
};

request(options, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  console.log('code: ' + res.statusCode);
});
