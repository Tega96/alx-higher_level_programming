#!/usr/bin/node

/**
 * Create a boolean variable: isInteger
 * check if it's string or space; set to false
 */

const [input] = process.argv.slice(2);
const isInt = (str) => {
  if (!str || typeof str !== 'string' || str.trim() === '') return false;

  const trimmed = str.trim();
  const num = +trimmed;

  return Number.isFinite(num) &&
    num === Math.floor(num) &&
    trimmed === num.toString();
};

if (input !== undefined && isInt(input)) {
  console.log(`My number: ${parseInt(input, 10)}`);
} else {
  console.log('Not a number');
}
