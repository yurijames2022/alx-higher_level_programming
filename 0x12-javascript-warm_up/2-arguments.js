#!/usr/bin/node
const listArgs = process.argv;
if (listArgs.length === 2) {
  console.log('No argument');
} else if (listArgs.length === 3) {
  console.log('Argument found');
} else if (listArgs.length > 3) {
  console.log('Arguments found');
}
