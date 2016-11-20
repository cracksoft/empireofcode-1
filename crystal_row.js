"use strict";

function checkLine(line) {
  var x = 0;
  for (var i in line) {
    if (x === line[i]) return false;
    x = line[i];
  }
  return true; 
}

var assert = require('assert');

if (!global.is_checking) {
  // These "asserts" using only for self-checking and not necessary for auto-testing
  assert.equal(checkLine(["X", "Z", "X"]), true, "1st example");
  assert.equal(checkLine(["X", "Z", "X", "X"]), false, "2nd example");
  assert.equal(checkLine(["X", "Z"]), true, "3rd example");
  assert.equal(checkLine(["Z", "X"]), true, "4th example");
  assert.equal(checkLine(["Z", "X", "Z", "X", "Z", "Z", "X"]), false, "5th example");
  console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}
