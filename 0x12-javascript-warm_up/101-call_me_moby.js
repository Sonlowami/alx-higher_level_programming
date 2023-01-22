#!/usr/bin/node
/* Execute a function x number of times */
exports.callMeMoby = function (x, theFunction) {
  if (typeof x === 'number') {
    for (let i = 0; i < x; i++) { theFunction(); }
  }
};
