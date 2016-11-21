"use strict";

function listCombination(arr1, arr2) {
  var r = [];

  for (var i in arr1) {
    r.push(arr1[i]);
    r.push(arr2[i]);
  }
  return r;
}

var assert = require('assert');

if (!global.is_checking) {
  assert.deepEqual(listCombination([1, 2, 3], [4, 5, 6]), [1, 4, 2, 5, 3, 6], "First");
  assert.deepEqual(listCombination([1, 1, 1, 1], [2, 2, 2, 2]), [1, 2, 1, 2, 1, 2, 1, 2], "Second");
  console.log("All set? Click \"Check\" to review your code and earn rewards!");
}
