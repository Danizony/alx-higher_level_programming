#!/usr/bin/node
const arg1 = process.argv.length;

if (arg1 > 2) {
  console.log('Argument' + (arg1 > 3 ? 's' : '') + ' found');
} else {
  console.log('No argument');
}
