"use strict";

function weakPoint(matrix) {
    var maxIndex = matrix.length - 1;
    var result = [];
    var minResult = 9999999;

    for (var i = maxIndex; i >= 0; i--) {
        for (var j = maxIndex; j >= 0; j--) {
            var summRow = 0;
            var summCol = 0;
            for (var indexRow = 0; indexRow <= maxIndex; indexRow++) {
                summRow = summRow + matrix[indexRow][j];
            }
            for (var indexCol = 0; indexCol <= maxIndex; indexCol++) {
                summCol = summCol + matrix[i][indexCol];
            }
            if (minResult >= (summCol + summRow)) {
                minResult = summCol + summRow;
                result = [i, j];
            }
        }
    }

    return result;
}

var assert = require('assert');

if (!global.is_checking) {
    assert.deepEqual(weakPoint([
        [7, 2, 7, 2, 8],
        [2, 9, 4, 1, 7],
        [3, 8, 6, 2, 4],
        [2, 5, 2, 9, 1],
        [6, 6, 5, 4, 5]]
    ), [3, 3], "Example");
    assert.deepEqual(weakPoint([
        [7, 2, 4, 2, 8],
        [2, 8, 1, 1, 7],
        [3, 8, 6, 2, 4],
        [2, 5, 2, 9, 1],
        [6, 6, 5, 4, 5]]
    ), [1, 2], "Two weak point");

    assert.deepEqual(weakPoint([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]]
    ), [0, 0], "Top left");

}
