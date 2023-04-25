#!/usr/bin/node
/**
 * This script prints the number of movies where a character with id 18
 * appears
 */
const request = require('request');
const id = 18;

const options = {
  // the url
  url: 'https://swapi-api.alx-tools.com/api/films/',
  // the headers
  headers: { Accept: 'application/json' }
};
request(options, (err, resp, body) => {
  const res = JSON.parse(body).results;
  let count = 0;
  res.forEach(item => {
    if (id in item.characters) { count++; }
  });
  console.log(count);
  if (err) { console.log(err); }
});
