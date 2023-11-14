#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js <fileA> <fileB> <fileC>');
  process.exit(1);
}

const fApath = process.argv[2];
const fBpath = process.argv[3];
const fCpath = process.argv[4];

const fileAContent = fs.readFileSync(fApath, 'utf-8');

const fileBContent = fs.readFileSync(fBpath, 'utf-8');

const concatenatedContent = fileAContent + fileBContent;

fs.writeFileSync(fCpath, concatenatedContent);

console.log(`Contents of ${fApath} and ${fBpath} concatenated to ${fCpath}`);
