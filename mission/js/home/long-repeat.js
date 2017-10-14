"use strict";

function longRepeat(line) {
    var maxRepeat = 0;
    var currentMaxRepeat = 0;
    var char = '';
    var prevChar = '';
    for (var i = 0; i < line.length; i++) {
        char = line.charAt(i);
        if (char === prevChar) {
            currentMaxRepeat++;
        } else {
             if (currentMaxRepeat <= maxRepeat) {
                currentMaxRepeat = 1;
            }
        }
        if (currentMaxRepeat > maxRepeat) {
            maxRepeat = currentMaxRepeat;
            currentMaxRepeat = char === prevChar ? currentMaxRepeat : 1;
        }
        prevChar = char;
    }
    return maxRepeat;
}

var assert = require('assert');

if (!global.is_checking) {
    assert.equal(longRepeat('sdsffffse'), 4, "First");
    assert.equal(longRepeat('ddvvrwwwrggg'), 3, "Second");
    assert.equal(longRepeat('aa'), 2, "3");
    console.log('"Run" is good. How is "Check"?');
}