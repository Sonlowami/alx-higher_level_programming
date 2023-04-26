#!/usr/bin/node
/**
 * This script gets an a filepath and attempts to read from it,
 * printing to stdout
 */
const fs = require('fs');
const args = process.argv.slice(2);

function read () {
  const data = fs.readFile(args[0],'utf-8', (err, content) => {
    if (err) { console.log(err); }
    else { console.log(content); }
  });
}
read();
