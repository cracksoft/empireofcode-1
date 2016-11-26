f=r=>r.match(/[A-Z][1-9]/g).reduce((x,y) => x+(y.charCodeAt(0)-65)*9+parseInt(y[1]),0)

function countReports(fullReport, fromDate, toDate) {
  return fullReport.split("\n")
    .map(x => x.split(" ")[0] >= fromDate && x.split(" ")[0] <= toDate ? f(x):0)
    .reduce((x, y) => x+y, 0);
}

var assert = require("assert");

if (!global.is_checking) {
  // These "asserts" using only for self-checking and not necessary for auto-testing
  assert.equal(countReports(
    "2015-01-01 A1,B2\n" +
    "2015-01-05 C3,C2,C1\n" +
    "2015-02-01 B4\n" +
    "2015-01-03 Z9,Z9",
    "2015-01-01", "2015-01-31"), 540, "Normal");
  assert.equal(countReports(
    "2000-02-02 Z2,Z1\n" +
    "2000-02-01 Z2,Z1\n" +
    "2000-02-03 Z2,Z1",
    "2000-02-04", "2000-02-28"), 0, "Zero");
  assert.equal(countReports("2999-12-31 Z9,A1", "2000-01-01", "2999-12-31"), 235, "Millenium");
  console.log("All set? Click 'Check' to review your code and earn rewards!");
}
