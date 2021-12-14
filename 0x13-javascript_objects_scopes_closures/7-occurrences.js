#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  let i;
  const len = list.length;
  for (i = 0; i < len; i++) {
    if (list[i] === searchElement) {
      counter++;
    }
  }
  return counter;
};
