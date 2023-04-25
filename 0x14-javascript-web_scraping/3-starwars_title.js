#!/usr/bin/node
/**
 * This script prints the title of a star wars episode with a given id
 * It expects the ID to be the 'only' commandline parameter
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
  console.log(res.title);
  if (err) { console.log(err); }
});
