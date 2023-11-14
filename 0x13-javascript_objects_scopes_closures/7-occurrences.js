#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let numbOfOccurrences = 0;

  for (const element of list) {
    if (element === searchElement) {
      numbOfOccurrences++;
    }
  }
  return (numbOfOccurrences);
};
