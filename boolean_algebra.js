"use strict";

var operationNames = ["conjunction", "disjunction", "implication", "exclusive", "equivalence"];

function boolean(x, y, operation){
  switch(operation[1]) {
    case 'o': return x&y;
    case 'i': return x|y;
    case 'm': return !(x&!y);
    case 'x': return x^y;
  }
  return x === y; 
}

var assert = require('assert');

if (!global.is_checking) {
  // These "asserts" using only for self-checking and not necessary for auto-testing
  assert.equal(boolean(1, 0, "conjunction"), 0, "and");
  assert.equal(boolean(1, 0, "disjunction"), 1, "or");
  assert.equal(boolean(1, 1, "implication"), 1, "material");
  assert.equal(boolean(0, 1, "exclusive"), 1, "xor");
  assert.equal(boolean(0, 1, "equivalence"), 0, "same?");
  assert.equal(boolean(0, 1, "implication"), 1, "moo");
  console.log("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!");
}
