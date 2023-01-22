#!/usr/bin/node
/**
 * class Square - create properties and methods to work with
 *		square objects
 */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle{

	constructor(size) {
		super(size, size);
	}
}
module.exports = Square;
