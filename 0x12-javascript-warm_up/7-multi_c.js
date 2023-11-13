#!/usr/bin/node

const process = require('node:process');
const count = parseInt(process.argv[2], 10);

if (count) {
  for (let i = 0; i < count; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
