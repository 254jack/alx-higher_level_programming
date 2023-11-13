#!/usr/bin/node

function factor(n) {
  if (n === 0) {
    return 1;
  }
  return n * factor(n - 1);
}

const num = parseInt(process.argv[2], 10);

if (!isNaN(num)) {
  console.log(factor(num));
} else {
  console.log(1);
}
