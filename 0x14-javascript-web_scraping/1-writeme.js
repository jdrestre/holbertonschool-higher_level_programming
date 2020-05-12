#!/usr/bin/node
const fs = require('fs');
const { error } = require('console');
fs.writeFile(process.argv[2], process.argv[3], error => {
    if (error) console.log(error);
});
