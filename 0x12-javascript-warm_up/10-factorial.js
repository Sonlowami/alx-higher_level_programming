#!/usr/bin/node
function factorial (n) {
  if (!n) { return (1); }
  return (n * factorial(n - 1));
}
const x = parseInt(process.argv[2]);
console.log(factorial(x));
