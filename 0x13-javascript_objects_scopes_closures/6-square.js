#!/usr/bin/node
const square = require('./5-square');
module.exports = class Square extends square {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

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
