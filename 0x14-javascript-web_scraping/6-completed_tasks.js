#!/usr/bin/node

const request = require('request');
const path = process.argv[2];
request(path, (_error, response, _body) => {
    const results = JSON.parse(response.body);
    let data = {};
    for (const result of results) {
        if (result.completed === true) {
            data[result.userId]
                ? (data[result.userId] = data[result.userId] + 1)
                : (data[result.userId] = 1);
        }
    }
    console.log(data);
});
