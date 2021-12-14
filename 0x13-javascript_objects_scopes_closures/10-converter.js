#!/usr/bin/node

exports.converter = function (base) {
  function Num (n) {
    return n.toString(base);
  }
  return Num;
};
