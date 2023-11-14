#!/usr/bin/node
exports.list = [1, 2, 3, 4, 5];
const originalList = require('./100-data').list;
console.log(originalList);
const mappedList = originalList.map (function (e, index) {
    return (e * index);
});
console.log(mappedList);