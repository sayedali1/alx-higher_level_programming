#!/usr/bin/node

function factorical (x) {
  if (x === 1 || isNaN(x)) {
    return 1;
  }
  if (x > 0) {
    return x * factorical(x - 1);
  }
}

const process = require('node:process');

console.log(factorical(parseInt(process.argv[2], 10)));
