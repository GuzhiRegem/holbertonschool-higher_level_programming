#!/usr/bin/node
let logMeCounter = -1;
exports.logMe = function (item) {
  logMeCounter++;
  console.log(logMeCounter + ': ' + item);
};
