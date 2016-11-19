"use strict";

function fizzBuzz(number) {
  let m3 = (number % 3 === 0);
  let m5 = (number % 5 === 0);
  if (m3 && m5) return "Fizz Buzz";
  if (m3) return "Fizz";
  if (m5) return "Buzz";
  return String(number);
}

var assert = require('assert');

if (!global.is_checking) {
  // These "asserts" using only for self-checking and not necessary for auto-testing
  assert.equal(fizzBuzz(15), "Fizz Buzz", "15 is divisible by 3 and 5");
  assert.equal(fizzBuzz(6), "Fizz", "6 is divisible by 3");
  assert.equal(fizzBuzz(5), "Buzz", "5 is divisible by 5");
  assert.equal(fizzBuzz(7), "7", "7 is not divisible by 3 or 5");
  console.log("Earn cool rewards by using the 'Check' button!");
}
