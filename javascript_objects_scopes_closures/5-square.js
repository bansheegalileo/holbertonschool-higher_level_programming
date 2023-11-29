#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    if (size <= 0 || !Number.isInteger(size)) {
      return {};
    }
    super(size, size);
  }
};
