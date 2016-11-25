"use strict";

function simpleAreas() {
  switch(arguments.length) {
    case 1:
      return (Math.round(Math.PI * 100 * arguments[0]/2 * arguments[0]/2)) / 100
    case 2:
      return Math.round(arguments[0] * arguments[1] * 100) / 100
  }
  let s = Array.prototype.reduce.call(arguments, (x,y) => x+y, 0)/2
  return Math.round(
    Math.sqrt(s * (s-arguments[0]) * (s-arguments[1]) * (s-arguments[2])) * 100)/100;
}

var assert = require('assert');

if (!global.is_checking) {
  // These "asserts" using only for self-checking and not necessary for auto-testing
  var almostEqual = function(actual, expected, significantDigits){
    significantDigits = significantDigits || 2;
    var precision =  Math.pow(0.1, significantDigits);
    return Math.abs(expected - actual) < precision;
  };

  assert(almostEqual(simpleAreas(3), 7.07), "Circle");
  assert(almostEqual(simpleAreas(2, 2), 4), "Square");
  assert(almostEqual(simpleAreas(2, 3), 6), "Rectangle");
  assert(almostEqual(simpleAreas(3, 5, 4), 6), "Triangle");
  assert(almostEqual(simpleAreas(1.5, 2.5, 2), 1.5), "Small triangle");
  console.log("All done? Earn rewards by using the 'Check' button!");
}
