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
  if (err) { console.log(err); }
  else { 
    const res = JSON.parse(body).results;
    let count = 0;
    res.forEach(item => {
      if (item.characters.find(character => character.endsWith('/18/')))
	    { count++; }
    });
    console.log(count);
  }
});
