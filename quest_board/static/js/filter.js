// Code obtained from https://codepen.io/tornadicshark/pen/XWboaRp?editors=1010 and modified to suit the project.
// Credit - Kassandra Flanders

document.addEventListener("DOMContentLoaded", function () {

    /*
    Takes the value of the selected checkbox within each category and stores it in an array.
    */
    function checkFilters() {
        // Location option checkboxes
        const checkCardiff = document.getElementById("cardiff").checked;
        const checkNewport = document.getElementById("newport").checked;
        const checkSwansea = document.getElementById("swansea").checked;
        const checkBridgend = document.getElementById("bridgend").checked;

        // Time option checkboxes
        const check10am = document.getElementById("10am").checked;
        const check12pm = document.getElementById("12pm").checked;
        const check2pm = document.getElementById("2pm").checked;
        const check4pm = document.getElementById("4pm").checked;

        // Experience option checkboxes
        const beginner = document.getElementById("beginner").checked;
        const everyone = document.getElementById("everyone").checked;
        const experienced = document.getElementById("experienced").checked;
        
        // Empty arrays to store the values of the checkboxes
        let locationFilters = [];
        let timeFilters = [];
        let expFilters = [];

        // If the location checkboxes are checked, push the corresponding value to the locationFilters array.
        if (checkCardiff) {
            locationFilters.push("cardiff");
        }
        if (checkNewport) {
            locationFilters.push("newport");
        }
        if (checkSwansea) {
            locationFilters.push("swansea");
        }
        if (checkBridgend) {
            locationFilters.push("bridgend");
        }

        // If the time checkboxes are checked, push the corresponding value to the timeFilters array.
        if (check10am) {
            timeFilters.push("10am");
        }
        if (check12pm) {
            timeFilters.push("12pm");
        }
        if (check2pm) {
            timeFilters.push("2pm");
        }
        if (check4pm) {
            timeFilters.push("4pm");
        }

        // If the experience checkboxes are checked, push the corresponding value to the expFilters array.
        if (beginner) {
            expFilters.push("beginner");
        }
        if (everyone) {
            expFilters.push("everyone");
        }
        if (experienced) {
            expFilters.push("experienced");
        }
    };
});