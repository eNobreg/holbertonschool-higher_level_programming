#!/usr/bin/node
exports.callMeMoby = function (x, theFucntion) {
  for (let i = 0; i < Number(x); i++) {
    theFucntion();
  }
};
