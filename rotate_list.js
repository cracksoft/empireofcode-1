"use strict";

function rotateList(elements, rotates) {
  return (elements.slice(rotates).concat(elements.slice(0, rotates)));
}
