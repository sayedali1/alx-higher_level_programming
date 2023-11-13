#!/usr/bin/node

function add(a, b) {
  return a + b;
}

const process = require('node:process');

console.log(add(parseInt(process.argv[2], 10), parseInt(process.argv[3], 10)));
