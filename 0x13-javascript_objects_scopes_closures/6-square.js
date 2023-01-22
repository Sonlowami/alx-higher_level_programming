#!/usr/bin/node
/**
 * class Square - create properties and methods to work with
 *		square objects
 */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle{

	/**
	 * constructor - create objects of type Square
	 * @size: size of the square
	*/
	constructor(size) {
		super(size, size);
	}
	/**
	 * charPrint - print a square with a character
	 * @c: the character to use
	 */
	charPrint(c) {
		if (!c)
			this.print();
		else
			this.printSqu(this.width, c);
	}
	/**
	 * printSqu - print a square
	 * @size: the size of the square
	 * @c: the character to use
	 */
	printSqu(size, c) {
		for (let i = 0; i < size; i++) {
			let str = '';
			for (let j = 0; j < size; j++)
				str += c;
			console.log(str);
		}
	}
}
module.exports = Square;
