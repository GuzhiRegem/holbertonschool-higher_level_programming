#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (!(Number.isInteger(w)) || !(Number.isInteger(h))) {
      return;
    }
    if ((w <= 0) || (h <= 0)) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let xP;
    let yP;
    for (yP = 0; yP < this.height; yP++) {
      let rowPrint = '';
      for (xP = 0; xP < this.width; xP++) {
        rowPrint += 'X';
      }
      console.log(rowPrint);
    }
  }

  rotate () {
    const wR = this.width;
    const hR = this.height;
    this.width = hR;
    this.height = wR;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
