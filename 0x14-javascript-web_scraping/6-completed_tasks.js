#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const out = {};
    const list = JSON.parse(body);
    for (let i = 0; list[i]; i++) {
      if (list[i].completed) {
        if (out[list[i].userId] === undefined) {
          out[list[i].userId] = 1;
        } else {
          out[list[i].userId]++;
        }
      }
    }
    console.log(out);
  }
});
