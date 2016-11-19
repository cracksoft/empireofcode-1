"use strict";

function doit(a, b, c) {
  return Math.round(Math.acos((b*b+c*c-a*a)/(2.0*b*c)) * 180.0 / Math.PI);

}

function angles(a, b, c){
  if ((a + b <= c) || (b + c <= a) || (c + a <= b))
    return [0, 0, 0];

  var r = [];
  r.push(doit(a, b, c));
  r.push(doit(b, c, a));
  r.push(doit(c, a, b));

  r.sort((a, b) => {return a-b;});

  return r;
}

var assert = require('assert');

if (!global.is_checking) {
  // These "asserts" using only for self-checking and not necessary for auto-testing
  assert.deepEqual(angles(4, 4, 4), [60, 60, 60], "All sides are equal");
  assert.deepEqual(angles(3, 4, 5), [37, 53, 90], "Egyptian triangle");
  assert.deepEqual(angles(2, 2, 5), [0, 0, 0], "It's can not be a triangle");
  console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}
