#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
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
