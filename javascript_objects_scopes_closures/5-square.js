#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    if (size <= 0 || !Number.isInteger(size)) {
      return {};
    }
    super(size, size);
  }
}

module.exports = Square;
