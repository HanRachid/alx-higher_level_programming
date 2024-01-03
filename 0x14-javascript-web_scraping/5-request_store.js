#!/usr/bin/node
const fs = require('node:fs');
const request = require('request');
const path = process.argv[2];
const file = process.argv[3];
request(path, (_error, response, _body) => {
    const result = response.body;
    fs.writeFileSync(file, result, { encoding: 'utf8' });
});
