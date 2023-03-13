#!/usr/bin/node

function addMeMaybe (n, theFunction) {
  n++;
  theFunction(n);
}

exports.addMeMaybe = addMeMaybe;
