#!/usr/bin/node

const args = process.argv.slice(2);

function secondBiggest (args) {
  if (!args[0] || !args[1]) {
    console.log(0);
    return;
  }
  let high = parseInt(args[0], 10);
  let low = high;
  for (let i = 1; i < args.length; i++) {
    if (parseInt(args[i], 10) > high) {
      const tmp = high;
      high = parseInt(args[i]);
      low = tmp;
    }
  }
  console.log(low);
}
secondBiggest(args);
