#!/usr/bin/node

const count = parseInt(process.argv[2], 10);

if (count) {
  for (let i = 0; i < count; i++) {
    let line = '';
    for (let j = 0; j < count; j++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
