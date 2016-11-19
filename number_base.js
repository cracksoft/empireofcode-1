"use strict";

function convert(strNumber, radix) {
  let arr = strNumber.split("").reverse();
  var r = 0;
  for (var i in arr) {
    let x = arr[i].charCodeAt(0);

    x -= (x >= 65)?55:48;
    console.log(x);
    if (x >= radix) return -1;
    r += x*Math.pow(radix,i);
  }
  return r;
}

var assert = require('assert');

if (!global.is_checking) {
  // These "asserts" using only for self-checking and not necessary for auto-testing
  assert.equal(convert("AF", 16), 175, "Hex");
  assert.equal(convert("101", 2), 5, "Bin");
  assert.equal(convert("101", 5), 26, "5 base");
  assert.equal(convert("Z", 36), 35, "Z base");
  assert.equal(convert("AB", 10), -1, "Z base");
  assert.equal(convert("909", 9), -1, "Z base");
  console.log("All done? Earn rewards by using the 'Check' button!");
}
