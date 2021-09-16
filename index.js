const pi = require('pi')

console.log(toString(pi(1000000)).match(/1/g).length)