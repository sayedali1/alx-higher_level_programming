#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurrences = 0;

  for (const elemet of list) {
    if (elemet === searchElement) {
      occurrences++;
    }
  }
  return occurrences;
};
