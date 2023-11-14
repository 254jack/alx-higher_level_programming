#!/usr/bin/node
const originalList = require('./100-data').list;

const mappedList = originalList.map((value, index) => value * index);

console.log(originalList);
console.log(mappedList);
