#!/usr/bin/env node

const first = parseInt(process.argv[2], 10);
if (isNaN(first)) {
  console.log('Missing number of occurances');
} else {
  for (let i = 0; i < first; i++) { console.log('C is fun'); }
}
