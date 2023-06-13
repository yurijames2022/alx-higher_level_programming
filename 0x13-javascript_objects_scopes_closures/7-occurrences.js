#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const current of list) {
    if (current === searchElement) {
      count++;
    }
  }
  return count;
};
