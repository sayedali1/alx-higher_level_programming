#!/usr/bin/node

const process = require('node:process');

if (process.argv.length > 2) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
