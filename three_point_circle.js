"use strict";

function pp(x) {
  return Math.round(x * 100)/100
}

function circleEquation(note) {
  let m = note.match(/\d/g)
  let x1 = m[0], x2 = m[2], x3 = m[4]
  let y1 = m[1], y2 = m[3], y3 = m[5]

  let a = x1*(y2-y3)-y1*(x2-x3)+x2*y3-x3*y2
  let b = ((x1*x1+y1*y1)*(y3-y2)+(x2*x2+y2*y2)*(y1-y3)+(x3*x3+y3*y3)*(y2-y1))/a
  let c = ((x1*x1+y1*y1)*(x2-x3)+(x2*x2+y2*y2)*(x3-x1)+(x3*x3+y3*y3)*(x1-x2))/a
  let d = ((x1*x1+y1*y1)*(x3*y2-x2*y3)+(x2*x2+y2*y2)*(x1*y3-x3*y1)+(x3*x3+y3*y3)*(x2*y1-x1*y2))/a

  let x = -b/2
  let y = -c/2
  let r = Math.sqrt((b*b+c*c-4*d)/4)

  return "(x-" + pp(x) + ")^2+(y-" + pp(y) + ")^2=" + pp(r) + "^2"
}

var assert = require("assert");

if (!global.is_checking) {
  // These "asserts" using only for self-checking and not necessary for auto-testing
  assert.equal(circleEquation("(2,2),(6,2),(2,6)"), "(x-4)^2+(y-4)^2=2.83^2", "1st example");
  assert.equal(circleEquation("(3,7),(6,9),(9,7)"), "(x-6)^2+(y-5.75)^2=3.25^2", "2nd example");
  console.log("Earn cool rewards by using the 'Check' button!");
}
