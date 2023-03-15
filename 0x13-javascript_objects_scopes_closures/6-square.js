#!/usr/bin/node

const Sq = require('./5-square');

class Square extends Sq {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        let line = '';
        for (let j = 0; j < this.width; j++) {
          line = line.concat(c);
        }
        console.log(line);
      }
    }
  }
}

module.exports = Square;
