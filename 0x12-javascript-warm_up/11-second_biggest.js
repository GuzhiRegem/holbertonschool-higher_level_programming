#!/usr/bin/node

const { argv } = require('process');
let i;
let second = 0;
if (argv.length > 3) {
  const list = [];
  for (i = 2; argv[i]; i++) {
    list.push(parseInt(argv[i]));
  }
  list.sort();
  second = list[i - 4];
}
console.log(second);
