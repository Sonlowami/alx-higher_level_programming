#!/usr/bin/node

exports.esrever = function (list) {
  let j = list.length - 1;
  for (let i = 0; i < j; i++, j--) {
    const tmp = list[i];
    list[i] = list[j];
    list[j] = tmp;
  }
  return list;
};
