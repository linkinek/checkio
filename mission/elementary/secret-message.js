"use strict";

function findMessage(data) {
    var symbols = "QWERTYUIOPASDFGHJKLZXCVBNM";
    var resut = '';
    for (let i = 0; i < data.length; i++) {
        let char = data[i];
        resut += symbols.indexOf(char) >= 0 ? char : '';
    }
    return resut;
}

var assert = require('assert');

if (!global.is_checking) {
    assert.equal(findMessage("How are you? Eh, ok. Low or Lower? Ohhh."), "HELLO", "hello");
    assert.equal(findMessage("hello world!"), "", "Nothing");
    assert.equal(findMessage("HELLO WORLD!!!"), "HELLOWORLD", "Capitals");
    console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}
