#!/usr/bin/node
const { argv } = require('process');

/* argv[0] => name of executable, argv[1] => path to the script */

if (argv[2] == null) {
  console.log('No argument');
} else if (process.argv.length === 3 && argv[3] == null) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
