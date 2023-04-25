#!/usr/bin/node
/*
 * This script computes each user with the number of tasks
 * completed.
 * Data is fetched from https://jsonplaceholder.typicode.com/todos
 */
const request = require('request');
const options = {
  url: 'https://jsonplaceholder.typicode.com/todos',
  headers: { Accept: 'application/json' }
};
request(options, (err, resp, body) => {
  const res = JSON.parse(body);
  const printable = {};
  let id = 1;
  let completed = 0;
  res.forEach(task => {
    if (task.userId === id && task.completed) {
      printable[`${id}`] = ++completed;
    } else if (task.userId > id) {
      completed = 0;
      id++;

      if (task.userId === id && task.completed) {
        printable[`${id}`] = ++completed;
      }
    }
  });
  console.log(printable);
  if (err) { console.log(err); }
});
