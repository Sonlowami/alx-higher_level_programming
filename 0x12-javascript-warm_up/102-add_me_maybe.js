#!/usr/bin/node
/**
 * addMeMaybe - increment a number and call a function
 * @n: the number to increment
 * @theFunction: funtion to call
 */
exports.addMeMaybe = function (n, theFunction) {
  if (typeof n === 'number') {
    n++;
    theFunction(n);
  }
};
