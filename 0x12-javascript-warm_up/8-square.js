#!/usr/bin/node
const mySize = parseInt(process.argv[2]);
let i = 0;
if (!mySize) {
  console.log('Missing size');
} else {
  while (i < mySize) {
    console.log('X');
    i++;
  }
}
