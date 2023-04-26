#!/usr/bin/node
/**
 * This script writes a string to a file
 * filepath will be the first commandline argument
 * content to write will be the second parameter
 */
const fs = require('fs');
const args = process.argv.slice(2);

const write = async (file, content) => {
  await fs.writeFile(file, content, (err, data) => {
    if (err) { console.log(err); }
  });
};
write(args[0], args[1]);
