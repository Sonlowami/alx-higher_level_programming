#!/usr/bin/node

const number = parseInt(process.argv[2]);

function factorial (n) {
  let fac = 1;
  if (isNaN(n)) { return (1); } else if (n <= 0) { return (1); }
  fac = n * factorial(n - 1);
  return fac;
}
console.log(factorial(number));
