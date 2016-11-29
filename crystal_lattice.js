function f(x){
  var z=0;
  for(var i in x){
    if(z === x[i]) return 1
    z = x[i]
  }
  return 0
}
function golf(g){
  var m = g.map((_,c)=>g.map(r=>r[c]))
  for (var i in g) if(f(g[i])) return 0
  for (var i in m) if(f(m[i])) return 0
  for (var i in m) {
    var x = m[i].map((_,c)=>m[i].map(r=>r[c]))
    for (var j in x) if(f(x[j])) return 0
  }
  return 1
}

var assert = require('assert');

if (!global.is_checking) {
  // These "asserts" using only for self-checking and not necessary for auto-testing
  assert.equal(golf([[["X", "Z"],
    ["Z", "X"]],
    [["Z", "X"],
      ["X", "Z"]]]), true, "1st example)");
  assert.equal(golf([[["X", "Z"],
    ["Z", "X"]],
    [["X", "Z"],
      ["Z", "X"]]]), false, "2nd example)");
  console.log("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!");
}
