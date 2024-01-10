#!/usr/bin/node
/**
 * This represents a rectangle with width and height as attributes.
 * If the height or width is equal to 0 or not positive integers
 * empty object is created.
 */
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
