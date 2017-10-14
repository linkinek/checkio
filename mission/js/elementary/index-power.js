"use strict";

function indexPower(array, n){
    return array.length - 1 >= n ? Math.pow(array[n], n) : -1;
}

var assert = require('assert');

if (!global.is_checking) {
    assert.equal(indexPower([1, 2, 3, 4], 2), 9, "Square");
    assert.equal(indexPower([1, 3, 10, 100], 3), 1000000, "Cube");
    assert.equal(indexPower([0, 1], 0), 1, "Zero power");
    assert.equal(indexPower([1, 2], 3), -1, "IndexError");
    console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}