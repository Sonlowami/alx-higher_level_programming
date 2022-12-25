#!/usr/bin/node
/* Change the value of a field in a const object */
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.value = 89;
console.log(myObject);
