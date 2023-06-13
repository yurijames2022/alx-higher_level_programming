#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      const ch = c.repeat(this.size);
      for (let i = 0; i < this.size; i++) {
        console.log(ch);
      }
    }
  }
};
