#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      const ch = c.repeat(this.width);
      for (let i = 0; i < this.width; i++) {
        console.log(ch);
      }
    }
  }
};
