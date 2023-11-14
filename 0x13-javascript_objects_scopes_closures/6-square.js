#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      super.print('X');
      return;
    }
    super.print(c);
  }
}

module.exports = Square;
