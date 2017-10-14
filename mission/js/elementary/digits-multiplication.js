"use strict";

function digitsMultip(data) {
    let dataString = data.toString();
    let result = 1;
    for (let i = 0; i < dataString.length; i++) {
        let buffer = Number(dataString[i]);
        result = buffer === 0 ? result : result * buffer;
    }
    return result;
}

var assert = require('assert');

if (!global.is_checking) {
    assert.equal(digitsMultip(123405), 120, "1st");
    assert.equal(digitsMultip(999), 729, "2nd");
    assert.equal(digitsMultip(1000), 1, "3rd");
    assert.equal(digitsMultip(1111), 1, "4th");
    console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}