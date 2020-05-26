/**
 * Use node factorial.js to excute
 */

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const fact = (number) => {
  if (number === 1 || number === -1 || number === 0) {
    return number;
  }

  let nextNum = 0;
  if (number > 0) {
    nextNum = number - 1;
  } else {
    nextNum = number + 1;
  }

  return number * fact(nextNum);
}

rl.question('Enter a number for calculate factorial: ', (number) => {
  console.log(`${number}! = ${fact(parseInt(number))}`);

  rl.close();
});
