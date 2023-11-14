#!/usr/bin/node

const Square_ = require('./5-square');

class Square extends Square_ {
  charPrint (c) {
    if (c === undefined) {
      super.print('X');
      return;
    }
    super.print(c);
  }
}

module.exports = Square;
