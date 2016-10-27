"use strict";

function sureNot(line) {
  console.log ((line.indexOf('not ') != 0 ? 'not ':'') + line);
  return ((line.indexOf('not ') != 0 ? 'not ':'') + line);
}
