"use strict";
function golf(n) {
  return parseInt((''+n).split("").reduce((x,y)=>x*=y!='0'?y:1))
}

var assert = require('assert');
//
if (!global.is_checking) {
  // These "asserts" using only for self-checking and not necessary for auto-testing
  assert.equal(golf(123405), 120, "1st example)");
  assert.equal(golf(999), 729, "2nd example");
  assert.equal(golf(1000), 1, "3rd example");
  assert.equal(golf(1111), 1, "4th example");
  console.log("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!");
}
