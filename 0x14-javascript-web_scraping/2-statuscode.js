#!/usr/bin/node

const request = require('request');
const path = process.argv[2];
request(path, (_error, response, _body) => {
    console.log('code: ' + response.statusCode);
});
