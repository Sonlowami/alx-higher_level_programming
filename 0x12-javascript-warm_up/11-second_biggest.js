#!/usr/bin/node

const args = process.argv.slice(2);

function secondBiggest (args) {
  if (!args[0] || !args[1]) {
    console.log(0);
    return;
  }
  let high = args[0];
  let low = args[0];
  for (let i = 1; i < args.length; i++) {
    if (args[i] > high) {
      const tmp = high;
      high = args[i];
      low = tmp;
    }
  }
  console.log(low);
}
secondBiggest(args);
