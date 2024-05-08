const _carId = Symbol('carId');

export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
    this[_carId] = Math.random().toString(36).substring(7);
  }

  cloneCar() {
    const clone = new Car(this._brand, this._motor, this._color);
    clone[_carId] = this[_carId];
    return clone;
  }
}
