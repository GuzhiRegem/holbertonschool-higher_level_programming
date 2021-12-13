#!/usr/bin/node

const { argv } = require('process');
const amnt = parseInt(argv[2]);
let x, y;
if (isNaN(amnt)) {
  console.log('Missing size');
} else {
  for (y = 0; y < amnt; y++) {
    let out = '';
    for (x = 0; x < amnt; x++) {
      out += 'X';
    }
    console.log(out);
  }
}
