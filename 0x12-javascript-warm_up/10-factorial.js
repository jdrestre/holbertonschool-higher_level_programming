#!/usr/bin/node
/* Script that computes and prints a factorial */
const argument = Number(process.argv[2]);
function factorial (num) {
  if (num === 0 || isNaN(num)) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

console.log(factorial(argument));
