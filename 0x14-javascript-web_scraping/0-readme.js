#!/usr/bin/node
let fs = require('fs');
let filename = process.argv[2]
fs.readFile(filename, 'utf8' , (err, data) => {
    if (err) {
      console.error(err)
      return
    }
    console.log(data)
  })