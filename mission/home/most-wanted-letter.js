"use strict";

function mostWanted(data) {
    data = data.toLowerCase();
    var resultChar = 'zz';
    var maxAttempts = 0;
    for(var i = 0; i < data.length; i++) {
        var char = data.charAt(i);
        if (isTrue(char)) {
            var tempMaxAttempt = 0;
            for (var j = 0; j < data.length; j++) {
                if (data[j] === char) {
                    tempMaxAttempt++;
                }
            }
            if (tempMaxAttempt > maxAttempts || (tempMaxAttempt === maxAttempts && char < resultChar)) {
                maxAttempts = tempMaxAttempt;
                resultChar = char;
            }
        }
    }

    return resultChar;
}

function isTrue(key) {
    var alfavit = 'qwertyuiopasdfghjklzxcvbnm';
    return alfavit.indexOf(key) > -1;
}

var assert = require('assert');

if (!global.is_checking) {
    assert.equal(mostWanted("Hello World!"), "l", "1st example");
    assert.equal(mostWanted("How do you do?"), "o", "2nd example");
    assert.equal(mostWanted("One"), "e", "3rd example");
    assert.equal(mostWanted("Oops!"), "o", "4th example");
    assert.equal(mostWanted("AAaooo!!!!"), "a", "Letters");
    console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}
