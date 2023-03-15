#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let word = '';
      for (let j = 0; j < this.width; j++) {
        word = word.concat('X');
      }
      console.log(word);
    }
  }
}

module.exports = Rectangle;
