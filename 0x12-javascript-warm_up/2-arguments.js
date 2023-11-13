#!/usr/bin/node

const process = require('node:process');

if (process.argv.length >= 3) {
  console.log('Argument found');
} else {
  console.log('No Argument');
}
