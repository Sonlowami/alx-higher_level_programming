#!/usr/bin/node
/**
 * This script prints the number of movies where a character with id 18
 * appears
 */
const request = require('request');

const options = {
  // the url
  url: 'https://swapi-api.alx-tools.com/api/films/',
  // the headers
  headers: { Accept: 'application/json' }
};
request(options, (err, resp, body) => {
  const id = process.argv[2];
  const res = JSON.parse(body).results;
  const characters = res[Number(`${id}`)].characters;

  characters.forEach(url => {
    request(url, (err, resp, body) => {
      const person = JSON.parse(body);
      console.log(person.name);
      if (err) { console.log(err); }
    });
  });
  if (err) { console.log(err); }
});
