#!/usr/bin/node

// Script to print the first argument
const [args] = process.argv.slice(2);

if (args === undefined) {
  console.log('No argument');
} else {
  console.log(args);
}
