#!/usr/bin/node
const fs = require('node:fs');
const path = process.argv[2];
const str = process.argv[3];
fs.writeFileSync(path, str, { encoding: 'utf8' });
