#!/usr/bin/node

let arg = -1;

exports.logMe = function (item) {
  arg++;
  console.log(arg + ':' + item);
};
