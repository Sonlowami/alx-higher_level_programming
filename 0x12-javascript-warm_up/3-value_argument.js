#!/usr/bin/node
const myVar = process.argv;
if (!myVar[2]) {
  console.log('No argument');
} else {
  console.log(myVar[2]);
}
