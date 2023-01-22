#!/usr/bin/node
/* Print the second largest argument */

const args = process.argv.slice(2);
const intargs = [];
if (!args.length || args.length === 1) { console.log(0); } else {
  for (let i = 0; i < args.length; i++) {
    const arg = parseInt(args[i]);
    if (arg) { intargs.push(arg); }
  }
}
let max, preMax;
if (intargs.length > 1) {
  max = intargs[0];
  for (let i = 1; i < intargs.length; i++) {
    if (intargs[i] > max) {
      preMax = max;
      max = intargs[i];
    }
  }
  console.log(preMax);
}
