"use strict";

function threeWords(data) {
    let dataArray = data.split(" ");
    var count = 0;
    var returnResult = false;
    dataArray.forEach(function (item) {
        if (isNaN(Number(item))) {
            count++;
            if (count === 3) {
                returnResult = true;
            }
        } else {
            count = 0;
        }
    });
    return returnResult;
}

var assert = require('assert');

if (!global.is_checking) {
    assert.equal(threeWords("Hello World hello"), true, "1st example");
    assert.equal(threeWords("He is 123 man"), false, "2nd example");
    assert.equal(threeWords("1 2 3 4"), false, "3rd example");
    assert.equal(threeWords("bla bla bla bla"), true, "4th example");
    assert.equal(threeWords("Hi"), false, "Letters");
    console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}