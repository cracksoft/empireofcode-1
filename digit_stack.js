function golf(c){
  var k=[],t=0
  for (var i in c) {
    let y=c[i].length
    if (y>4) k.push(parseInt(c[i].split(" ")[1]))
    else t+=k.length>0?(y<4?k.pop():k.slice(-1)[0]):0
  }
  return t;
}

var assert = require('assert');

if (!global.is_checking){
  // These "asserts" using only for self-checking and not necessary for auto-testing
  assert.equal(golf(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK", "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]), 8, "Example");
  assert.equal(golf(["POP", "POP"]), 0, "PopPop");
  assert.equal(golf(["PUSH 9", "PUSH 9", "POP"]), 9, "Push 9");
  assert.equal(golf([]), 0, "Empty");
  console.log("Code's finished? Earn rewards by clicking 'Check' to review your tests!");
}
