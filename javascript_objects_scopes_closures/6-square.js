#!/usr/bin/node

const Square = require('./5-square');

module.exports = class Sixquare extends Square {
  charPrint (c) {
    const printChar = c || 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(printChar.repeat(this.width));
    }
  }
}
