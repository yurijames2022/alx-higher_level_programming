#!/usr/bin/node
const BigSquare = require('./5-square');
module.exports = class Square extends BigSquare {
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      const ch = c.repeat(this.size);
      for (let i = 0; i < this.size; i++) {
        console.log(ch);
      }
    }
  }
};
