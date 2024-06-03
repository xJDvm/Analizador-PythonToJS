function greet(name) {
    if (name) {
        return "Hello, " + name + "!";
    } else {
        return "Hello, world!";
    }
}

let userName = "Alice";
console.log(greet(userName));

let sum = 5 + 10;
let product = sum * 2;
let division = product / 4;
let remainder = division % 3;
// hola
let bool = true && false || true;
console.log("Sum:", sum, "Product:", product, "Division:", division, "Remainder:", remainder);
