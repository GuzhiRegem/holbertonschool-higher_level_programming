#!/usr/bin/node
const request = require('request');
const num = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films';
request(url, function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    for (let i = 0; results[i]; i++) {
      if (i + 1 === parseInt(num)) {
        const chars = results[i].characters;
        for (let e = 0; chars[e]; e++) {
          request(chars[e], function (error, response, body) {
            if (!error) {
              console.log(JSON.parse(body).name);
            }
          });
        }
      }
    }
  }
});
