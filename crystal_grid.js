"use strict";

function checkLine(line) {
  var x = 0;
  for (var i in line) {
    if (x === line[i]) return false;
    x = line[i];
  }
  return true; 
}

function checkGrid(grid) {
  let m=grid[0].map((_,c) => grid.map(r => r[c]));

  for (var i in grid) {
    if (!checkLine(grid[i])) return false;
  }
  for (var i in m) {
    if (!checkLine(m[i])) return false;
  }
  return true;
}

var assert = require('assert');

if (!global.is_checking) {
  // These "asserts" using only for self-checking and not necessary for auto-testing
  assert.equal(checkGrid([["X", "Z"], ["Z", "X"]]), true, "2x2 Good");
  assert.equal(checkGrid([
    ["X", "Z", "X"],
    ["Z", "X", "Z"],
    ["X", "Z", "X"]]), true, "3x3 Good");
  assert.equal(checkGrid([
    ["X", "Z", "X", "Z"],
    ["Z", "X", "Z", "X"]]), true, "2x4 Good");
  assert.equal(checkGrid([
    ["X", "X"],
    ["X", "X"]]), false, "2x2 Bad");
  assert.equal(checkGrid([
    ["X", "Z", "X"],
    ["Z", "Z", "Z"],
    ["X", "Z", "X"]]), false, "3x3 Bad");
  assert.equal(checkGrid([
    ["X", "Z", "X", "Z"],
    ["X", "Z", "X", "Z"]]), false, "2x4 Bad");
  console.log("Use 'Check' to earn sweet rewards!");
}
