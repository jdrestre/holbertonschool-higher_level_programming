#!/usr/bin/node
/* Script that prints the first argument passed to it */
const arg2 = process.argv[2];
if (arg2) {
  console.log(arg2);
} else {
  console.log('No argument');
}
