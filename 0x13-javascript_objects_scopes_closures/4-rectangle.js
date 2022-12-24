#!/usr/bin/node
/**
 * Class Rectangle - represent objects of type rectangle
 */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let myString = '';
      for (let j = 0; j < this.width; j++) {
        myString += 'X';
      }
      console.log(myString);
    }
  }

  rotate () {
    const x = this.width;
    this.width = this.height;
    this.height = x;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
