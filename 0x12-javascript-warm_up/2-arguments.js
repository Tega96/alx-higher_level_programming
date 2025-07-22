#!/usr/bin/node

// Script to print message depending on number of arguments passed
const argv = process.argv.slice(2);

// print process.arg
if (argv.length === 0) {
	console.log('No argument');
}else if (argv.length === 1) {
	console.log('Argument found');
}else {
	console.log('Arguments found');
}
