#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];
  const end = list.length - 1;

  for (let i = 0; i <= end; i++) {
    revList[i] = list[end - i];
  }
  return (revList);
};
