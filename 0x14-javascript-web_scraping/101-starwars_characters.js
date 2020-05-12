#!/usr/bin/node
const request = require('request');

const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + process.argv[2]
};

request(options, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const json = JSON.parse(body);
    for (const entry of json.characters) {
      request(entry, function (err, res, body) {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
