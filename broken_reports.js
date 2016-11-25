golf=r=>r.match(/[A-Z][1-9]/g).reduce((x,y) => x+(y.charCodeAt(0)-65)*9+parseInt(y[1]),0)

var assert = require("assert");
if (!global.is_checking) {
  // These "asserts" using only for self-checking and not necessary for auto-testing
  assert.equal(golf("ASDA1,BB22D01C1"), 31, "1st example");
  assert.equal(golf("B1,C2,D3"), 60, "2nd example");
  console.log("Code's finished? Earn rewards by clicking 'Check' to review your tests!");
}
