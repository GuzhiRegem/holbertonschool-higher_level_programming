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
};
