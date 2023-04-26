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
  if (!err) {
    const res = JSON.parse(body);
    const characters = res.characters;
    printName(characters, 0);
  }
});
function printName (array, index) {
  request(array[index], (err, resp, data) => {
    if (!err) {
      console.log(JSON.parse(data).name);
    }
    if (index < array.length - 1) {
      printName(array, index + 1);
    }
  });
}
