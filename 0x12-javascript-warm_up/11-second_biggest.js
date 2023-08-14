#!/usr/bin/node

function secMax (array) {
  if (array.length < 2) {
    return (0);
  } else {
    array.sort((x, y) => x - y);
    array.pop();
    return (array.pop());
  }
}

const nArray = process.argv.slice(2);

console.log(secMax(nArray));
