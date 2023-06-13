#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const x = 'X'.repeat(this.width);
    let i = 0;
    while (i < this.height) {
      console.log(x);
      i++;
    }
  }
}
module.exports = Rectangle;
