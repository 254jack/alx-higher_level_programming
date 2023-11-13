#!/usr/bin/node
const occurrences = parseInt(process.argv[2], 10);

if (!isNaN(occurrences) && occurrences > 0) {
  for (let i = 0; i < occurrences; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
