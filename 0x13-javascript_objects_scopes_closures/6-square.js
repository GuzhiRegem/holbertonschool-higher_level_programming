#!/usr/bin/node
const SquareClass = require('./5-square');

module.exports = class Square extends SquareClass {
  charPrint (c) {
    let charP = 'X';
    if (c !== undefined) {
      charP = c;
    }
    let xP;
    let yP;
    for (yP = 0; yP < this.height; yP++) {
      let rowPrint = '';
      for (xP = 0; xP < this.width; xP++) {
        rowPrint += charP;
      }
      console.log(rowPrint);
    }
  }
};
