#!/usr/bin/node

exports.esrever = function (list) {
  const out = [];
  let i;
  const len = list.length;
  for (i = len - 1; i >= 0; i--) {
    out.push(list[i]);
  }
  return out;
};
