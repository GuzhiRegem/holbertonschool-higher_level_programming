#!/usr/bin/node
const request = require('request');
const num = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films';
request(url, function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    for (let i = 0; results[i]; i++) {
      if (results[i].episode_id === parseInt(num)) {
        console.log(results[i].title);
      }
    }
  }
});
