#!/usr/bin/node
/**
 * This script prints the number of movies where a character with id 18
 * appears
 */
const request = require('request');
const id = process.argv[2];
const options = {
  // the url
  url: `https://swapi-api.alx-tools.com/api/films/${id}`,
  // the headers
  headers: { Accept: 'application/json' }
};
request(options, (err, resp, body) => {
  const res = JSON.parse(body);
  const characters = res.characters;

  characters.forEach(url => {
    request(url, (err, resp, body) => {
      const person = JSON.parse(body);
      console.log(person.name);
      if (err) { console.log(err); }
    });
  });
  if (err) { console.log(err); }
});
