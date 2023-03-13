#!/usr/bin/node

const first = parseInt(process.argv[2], 10);
if (isNaN(first)) {
  console.log('Missing size');
} else {
  for (let i = 0, tmp = ''; i < first; i++) {
    for (let j = 0; j < first; j++) { tmp += 'X'; }
    console.log(tmp);
    tmp = '';
  }
}
