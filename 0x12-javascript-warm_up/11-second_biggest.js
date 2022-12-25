#!/usr/bin/node
const args = parseInt(process.argv.slice(2));
if (!args[0] || !args[1]) {
  console.log(0);
}
console.log(args);
let max = args[0];
let prevmax;
for (let i = 1; args[i]; i++) {
  if (args[i] > max) {
    prevmax = max;
    max = args[i];
  }
}
console.log(prevmax);
