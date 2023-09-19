#!/usr/bin/node
const fs = require('fs');

// Get the file path of the first argument
const filePath = process.argv[2];

// Read and display file contents
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
