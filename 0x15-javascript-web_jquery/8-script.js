#!/usr/bin/node
$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (const entry of data.results) {
    $('UL#list_movies').append('<li>' + entry.title + '</li>');
  }
});
