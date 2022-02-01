#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const search = 'https://swapi-api.hbtn.io/api/people/18/';
request(url, function (error, response, body) {
  if (!error) {
    let count = 0;
    const results = JSON.parse(body).results;
    for (let i = 0; results[i]; i++) {
      if (results[i].characters.includes(search)) {
        count += 1;
      }
    }
    console.log(count);
  }
});
