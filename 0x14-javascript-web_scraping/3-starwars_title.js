#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const path = 'https://swapi-api.alx-tools.com/api/films/' + id;
request(path, (_error, response, _body) => {
  const title = JSON.parse(response.body).title;
  console.log(title);
});
