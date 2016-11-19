"use strict";

function mostDifference() {
  let arr = Array.prototype.slice.call(arguments);

  return arr.length?(Math.max.apply(null, arr) - Math.min.apply(null, arr)):0;
}

var assert = require('assert');

if (!global.is_checking) {
  // These "asserts" using only for self-checking and not necessary for auto-testing
  var almostEqual = function(actual, expected, significantDigits){
    significantDigits = significantDigits || 3;
    var precision =  Math.pow(0.1, significantDigits);
    return Math.abs(expected - actual) < precision;
  };

  assert(almostEqual(mostDifference(1, 2, 3), 2), "3-1=2");
  assert(almostEqual(mostDifference(5, 5), 0), "5-5=0");
  assert(almostEqual(mostDifference(10.2, 2.2, 0.00001, 1.1, 0.5), 10.199), "10.2-(0.00001)=10.19999");
  assert(almostEqual(mostDifference(), 0), "Empty");
  console.log("Use 'Check' to earn sweet rewards!");
}
