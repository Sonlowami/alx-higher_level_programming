#!/usr/bin/node

exports.converter = function (base) {
  function actualConverter (n) {
    return n.toString(base);
  }
  return actualConverter;
};
