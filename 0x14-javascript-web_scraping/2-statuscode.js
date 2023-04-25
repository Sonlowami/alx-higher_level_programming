#!/usr/bin/node
/**
 * This script displays the status code of a GET request
 * It expects the URL to fetch from to be passed as the 'only'
 * argument on the commandline
 */
const request = require('request');
const args = process.argv.slice(2);

request(args[0], (err, resp, body) => {
  console.log('code: ', resp && resp.statusCode);
  if (err) { console.log(err); }
});
