"use strict";

function evenLast(data) {
    return !data.length ? 0 : process();

    function process() {
        let lastElement = data[data.length - 1];
        return data.filter(function (element, index) {
            return index % 2 === 0;
        }).reduce(function (a, b) {
            return a + b;
        }) * lastElement;
    }
}

var assert = require('assert');

if (!global.is_checking) {
    assert.equal(evenLast([0, 1, 2, 3, 4, 5]), 30, "(0+2+4)*5=30");
    assert.equal(evenLast([1, 3, 5]), 30, "(1+5)*5=30");
    assert.equal(evenLast([6]), 36, "(6)*6=36");
    assert.equal(evenLast([]), 0, "An empty array = 0");
    console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}