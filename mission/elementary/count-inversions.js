"use strict";

function countInversion(sequence){
    let sum = 0;
    for (let i = 0; i < sequence.length; i++) {
        let number = sequence[i];
        for (let j = i; j < sequence.length; j++) {
            sum = number > sequence[j] ? sum + 1 : sum;
        }
    }
    return sum;
}

var assert = require('assert');

if (!global.is_checking) {
    assert.equal(countInversion([1, 2, 5, 3, 4, 7, 6]), 3, "Example");
    assert.equal(countInversion([0, 1, 2, 3]), 0, "Sorted");
    assert.equal(countInversion([99, -99]), 1, "Two numbers");
    assert.equal(countInversion([5, 3, 2, 1, 0]), 10, "Reversed");
    console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}