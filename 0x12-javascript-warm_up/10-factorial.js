#!/usr/bin/node

function factorial (num) {
  if (isNaN(num) || num === 0) {
    return (1);
  } else {
    return (num * factorial(num - 1));
  }
}

const num = parseInt(process.argv[2], 10);

console.log(factorial(num));
