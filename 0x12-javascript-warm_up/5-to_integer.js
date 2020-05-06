#!/user/bin/node
/* Script that prints **`My number`: `<first argument converted in integer>`** if the first argument can be converted to an integer */
const num2 = Number(process.argv[2]);
const arg2 = process.argv[2];
if (arg2 && num2) {
  console.log('My number: ' + arg2);
} else {
  console.log('Not a number');
}
