#!/usr/bin/node

if (process.argv.length <= 2) {
  console.log(0);
} else {
  let maxNum = parseInt(process.argv[2], 10);
  for (let i = 3; i < process.argv.length; i++) {
    if (parseInt(process.argv[i], 10) > maxNum) {
      maxNum = parseInt(process.argv[i], 10);
    }
  }
  console.log(maxNum);
}
