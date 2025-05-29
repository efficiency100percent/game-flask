// script.js

function calculateBMI() {
    // Get height and weight inputs from the HTML form
    var heightInput = document.getElementById("h-input").value;
    var weightInput = document.getElementById("w-input").value;

    // Convert height from centimeters to meters
    var heightInMeters = heightInput / 100;

    // Calculate BMI
    var bmi = weightInput / (heightInMeters * heightInMeters);

    // Display BMI value on the webpage
    var bmiOutput = document.getElementById("bmi-output");
    bmiOutput.textContent = bmi.toFixed(2);

    // Determine the BMI status and display it
    var statusOutput = document.getElementById("bmi-status");
    if (bmi < 18.5) {
        statusOutput.textContent = "Underweight";
    } else if (bmi >= 18.5 && bmi < 24.9) {
        statusOutput.textContent = "Normal Weight";
    } else if (bmi >= 25 && bmi < 29.9) {
        statusOutput.textContent = "Overweight";
    } else {
        statusOutput.textContent = "Obese";
    }
}

// Add an event listener to the "Calculate BMI" button
var calculateButton = document.querySelector("button");
calculateButton.addEventListener("click", calculateBMI);