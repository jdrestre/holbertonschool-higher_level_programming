#!/usr/bin/node
/* Script that prints x times “C is fun” */
let i = 0;
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  while (i < process.argv[2]) {
    console.log('C is fun');
    i++;
  }
}
