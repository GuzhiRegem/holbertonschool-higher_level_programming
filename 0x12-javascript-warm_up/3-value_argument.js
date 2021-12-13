#!/usr/bin/node

const { argv } = require('process');
const out = argv[2];
if (out !== undefined) {
  console.log(out);
} else {
  console.log('No argument');
}
