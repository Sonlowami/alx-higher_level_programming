#!/usr/bin/node
const myVar = process.argv;
if (!myVar[2]) {
  console.log('No argument');
} else if (myVar[3]) {
  console.log('Arguments found');
} else {
  console.log('Argument found');
}
