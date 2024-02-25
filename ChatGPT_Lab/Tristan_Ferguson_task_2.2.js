// Represents a car
class Car {
  /**
   * Create a car.
   * @param {string} brand - The brand of the car.
   */
  constructor(brand) {
    this.carname = brand;
  }

  /**
   * Present the car.
   * @returns {string} A string representing the car.
   */
  present() {
    return 'I have a ' + this.carname;
  }
}

// Represents a car model, extending Car class
class Model extends Car {
  /**
   * Create a car model.
   * @param {string} brand - The brand of the car.
   * @param {string} mod - The model of the car.
   */
  constructor(brand, mod) {
    super(brand);
    this.model = mod;
  }

  /**
   * Show the car model.
   * @returns {string} A string representing the car model.
   */
  show() {
    return this.present() + ', it is a ' + this.model;
  }
}

// Create an instance of Model
let myCar = new Model("Ford", "Mustang");

// Display the car model on the webpage
document.getElementById("demo").innerHTML = myCar.show();
