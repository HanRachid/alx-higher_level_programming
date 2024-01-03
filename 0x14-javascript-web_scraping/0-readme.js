#!/usr/bin/node

const fs = require('node:fs');
const file = fs.readFileSync(process.argv[2], { encoding: 'utf8' });

process.stdout.write(file);
