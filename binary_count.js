"use strict";

function countUnits(number) {
  var s = 0;
  while(number>0) {
    s+=(number&1);
    number/=2;
  }
  return s;
}

var assert = require('assert');

if (!global.is_checking) {
  // These "asserts" using only for self-checking and not necessary for auto-testing
  assert.equal(countUnits(4), 1, "0b100");
  assert.equal(countUnits(15), 4, "0b1111");
  assert.equal(countUnits(1), 1, "0b1");
  assert.equal(countUnits(1022), 9, "0b1111111110");
  console.log("Use 'Check' to earn sweet rewards!");
}
