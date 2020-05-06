#!/usr/bin/node
/* Script that prints the first argument passed to it */
const arg = process.argv.length;
const arg2 = process.argv[2];
if (arg <= 2) {
  console.log('No argument');
} else {
  console.log(arg2);
}
