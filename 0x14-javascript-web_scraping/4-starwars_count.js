#!/usr/bin/node

const request = require('request');
const path = process.argv[2];
request(path, (_error, response, _body) => {
    const results = JSON.parse(response.body).results;
    const count = results.filter((result) => {
        return result.characters.includes(
            'https://swapi-api.alx-tools.com/api/people/18/'
        );
    });
    console.log(count.length);
});
