#!/usr/bin/node
if (!parseInt(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  const x = parseInt(process.argv[2]);
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
