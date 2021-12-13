#!/usr/bin/node

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }
  if (n < 3) {
    return n;
  }
  return factorial(n - 1) * n;
}
const { argv } = require('process');
const num1 = parseInt(argv[2]);
console.log(factorial(num1));
