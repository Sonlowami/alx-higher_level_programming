#!/usr/bin/node

const fs = require('fs').promises;

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

async function read (filePath) {
  try {
    const fileContent = await fs.readFile(filePath);
    return fileContent.toString();
  } catch (error) { console.log(error.message); }
}

async function write (filePath, fileContent, options) {
  try {
    if (options === undefined) {
      await fs.writeFile(filePath, fileContent);
    } else { await fs.writeFile(filePath, fileContent, options); }
  } catch (error) { console.log(error.message); }
}

(async () => {
  await write(fileC, await read(fileA));
  await write(fileC, await read(fileB), { flag: 'a' });
})();
