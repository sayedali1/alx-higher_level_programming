#!/usr/bin/node
const fs = require('fs');

const file1 = fs.readFileSync(process.argv[2], 'utf-8');
const file2 = fs.readFileSync(process.argv[3], 'utf-8');

let file3 = file1.concat('\n');
file3 = file3.concat(file2);
fs.writeFileSync(process.argv[4], file3);
