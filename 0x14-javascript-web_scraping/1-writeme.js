#!/usr/bin/node
/**
 * This script writes a string to a file
 * filepath will be the first commandline argument
 * content to write will be the second parameter
 */
const fs = require('fs/promises');
const args = process.argv.slice(2);

const write = async (file, path) => {
  try {
    await fs.writeFile(file, path, { encoding: 'utf-8' });
  } catch (error) { console.log(error); }
};
write(args[0], args[1]);
