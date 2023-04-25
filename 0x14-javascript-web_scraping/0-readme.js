#!/usr/bin/node
/**
 * This script gets an a filepath and attempts to read from it,
 * printing to stdout
 */
const fs = require('fs/promises');
const args = process.argv.slice(2);

async function read () {
  try {
    const data = await fs.readFile(args[0], { encoding: 'utf-8' });
    await console.log(data);
  } catch (error) { console.log(error); }
}
read();
