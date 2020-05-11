#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w = 0, h = 0) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const saved = this.width;
    this.width = this.height;
    this.height = saved;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
