#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let total = 0;
  for (const x of list) {
    if (x === searchElement) {
      total += 1;
    }
  }
  return total;
};
