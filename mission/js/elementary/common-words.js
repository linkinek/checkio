"use strict";

function commonWords(first, second) {
    let result = "";
    let firstArray = first.split(",");
    let secondArray = second.split(",");
    firstArray.filter(sFirst => secondArray.includes(sFirst) > 0)
        .sort().forEach(t => result = result.length == 0 ? t : (result + "," + t));
    return result;
}

var assert = require('assert');

if (!global.is_checking) {
    assert.equal(commonWords("hello,world", "hello,earth"), "hello", "Hello");
    assert.equal(commonWords("one,two,three", "four,five,six"), "", "Too different");
    assert.equal(commonWords("one,two,three", "four,five,one,two,six,three"), "one,three,two", "1 2 3");
    console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}