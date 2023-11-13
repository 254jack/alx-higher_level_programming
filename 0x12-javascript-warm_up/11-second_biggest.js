#!/usr/bin/node

const nums = process.argv.slice(2).map(Number).map(Number);

nums.sort((a, b) => b - a);

const secondBggest = nums[1] || 0;

console.log(secondBggest);
