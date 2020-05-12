#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);

const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + args[0],
  method: 'GET',
  headers: {
    Accept: 'application/json'
  }
};

request(options, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const json = JSON.parse(body);
  console.log(json.title);
});
