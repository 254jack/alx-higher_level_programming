#!/usr/bin/node

const originalDict = require('./101-data').dict;

const occurrencesDict = {};

for (const userId in originalDict) {
  const occurrences = originalDict[userId];

  if (!occurrencesDict[occurrences]) {
    occurrencesDict[occurrences] = [];
  }

  occurrencesDict[occurrences].push(userId);
}

console.log(occurrencesDict);
