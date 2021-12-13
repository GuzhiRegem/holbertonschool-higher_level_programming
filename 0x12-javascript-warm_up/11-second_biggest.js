#!/usr/bin/node

const { argv } = require('process');
let i;
let max = parseInt(argv[2]);
let second = 0;
if (argv.length > 3) {
  second = parseInt(argv[3]);
  for (i = 2; argv[i]; i++) {
    const num = parseInt(argv[i]);
    if (num > max) {
      second = max;
      max = num;
    }
  }
}
console.log(second);
