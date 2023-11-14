#!/usr/bin/node

const list = require('./100-data.js').list;
const updatedList = list.map((element, index) => element * index);
console.log(list);
console.log(updatedList);
