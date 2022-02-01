#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (!error) {
    const out = {
      1: 0,
      2: 0,
      3: 0,
      4: 0,
      5: 0,
      6: 0,
      7: 0,
      8: 0,
      9: 0,
      10: 0
    };
    const list = JSON.parse(body);
    for (let i = 0; list[i]; i++) {
      const num = list[i].userId;
      if (list[i].completed) {
        out[num]++;
      }
    }
    console.log(out);
  }
});
