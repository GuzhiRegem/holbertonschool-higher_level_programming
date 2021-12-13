#!/usr/bin/node

const { argv } = require('process');
const amnt = parseInt(argv[2]);
let i;
if (isNaN(amnt)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < amnt; i++) {
    console.log('C is fun');
  }
}
