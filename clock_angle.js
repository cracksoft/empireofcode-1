"use strict";

function clockAngle(time){
  let t = time.split(':');
  let h = parseInt(t[0]);
  let m = parseInt(t[1]);

  if (h > 12) h -= 12;
  let r = Math.abs(0.5 * ((60*h) - (11*m)));

  if (r > 180) r = 360-r;
  return r;
}

var assert = require('assert');

if (!global.is_checking) {
  // These "asserts" using only for self-checking and not necessary for auto-testing
  assert.equal(clockAngle("02:30"), 105, "02:30");
  assert.equal(clockAngle("13:42"), 159, "13:42");
  assert.equal(clockAngle("01:42"), 159, "01:42");
  assert.equal(clockAngle("01:43"), 153.5, "01:43");
  assert.equal(clockAngle("00:00"), 0, "Zero");
  assert.equal(clockAngle("12:01"), 5.5, "Little later");
  assert.equal(clockAngle("18:00"), 180, "Opposite");
  console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}
