#!/usr/bin/node

const { argv } = require('process');
const out = parseInt(argv[2]);
if (isNaN(out)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + out);
}
