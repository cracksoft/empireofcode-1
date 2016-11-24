"use strict";

function isSkewSymmetric(matrix) {
  for (var i in matrix) {
    for (var j in matrix) {
      if ((i == j && matrix[i][j] !== 0) || (i !== j && matrix[i][j] !== -matrix[j][i])) {
        return false;
      }
    }
  }
  return true;
}

var assert = require("assert");

if (!global.is_checking) {
  // These "asserts" using only for self-checking and not necessary for auto-testing
  assert.equal(isSkewSymmetric([
    [0, 1, 2],
    [-1, 0, 1],
    [-2, -1, 0]]), true, "1st example");
  assert.equal(isSkewSymmetric([
    [0, 1, 2],
    [-1, 1, 1],
    [-2, -1, 0]]), false, "2nd example");
  assert.equal(isSkewSymmetric([
    [0, 1, 2],
    [-1, 0, 1],
    [-3, -1, 0]]), false, "3rd example");
  console.log("Earn cool rewards by using the 'Check' button!");
}
