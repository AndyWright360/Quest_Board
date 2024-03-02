// Code obtained from https://codepen.io/tornadicshark/pen/XWboaRp?editors=1010 and modified to suit the project.
// Credit - Kassandra Flanders

document.addEventListener("DOMContentLoaded", function () {

    // Hide no results message when page loads
    document.getElementById("no-results").style.display = "none";
    
    /*
    Takes the value of the selected checkbox within each category and stores it in an array. Passes each array into the filter function.
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

        if (locationFilters.length === 0 && timeFilters.length === 0 && expFilters.length === 0) {
            // Display all events and hide no results message if no filters are selected
            filter([""], timeFilters, expFilters);
            document.getElementById("no-results").style.display = "none";
            const event = document.getElementsByClassName("event-card");
            for (let i = 0; i < event.length; i++) {
                event[i].style.display = "grid";
            }
            
        } else {
            // Apply filters if any are selected
            filter(locationFilters, timeFilters, expFilters);
        }

    };

    /*
    This function checks the data-type attribute of each event card and compares it to each index value within the provided filter arrays. If a match is found, the card remains visible; otherwise, it is hidden.
    */
    function filter(locations, times, expLevels) {
        const event = document.getElementsByClassName("event-card");

        for (let i = 0; i < event.length; i++) {
            let matchFound = false;
            event[i].style.display = "none";

            // Compares the data-type value across each possible combination of selected filter options.
            for (let l = 0; l < locations.length; l++) {
                for (let t = 0; t < times.length; t++) {
                    for (let e = 0; e < expLevels.length; e++) {
                        if (event[i].getAttribute("data-location") === locations[l] &&
                        event[i].getAttribute("data-time") === times[t] &&
                        event[i].getAttribute("data-exp") === expLevels[e]) {
                            matchFound = true;
                        }
                    }
                }
            }

            if (locations.length === 0 && times.length === 0 && expLevels.length === 0) {
                matchFound = true; // If no filters selected, show all events
            } else if (locations.length === 0 && times.length === 0) {
                for (let e = 0; e < expLevels.length; e++) {
                    if (event[i].getAttribute("data-exp") === expLevels[e]) {
                        matchFound = true;
                    }
                }
            } else if (locations.length === 0 && expLevels.length === 0) {
                for (let t = 0; t < times.length; t++) {
                    if (event[i].getAttribute("data-time") === times[t]) {
                        matchFound = true;
                    }
                }
            } else if (times.length === 0 && expLevels.length === 0) {
                for (let l = 0; l < locations.length; l++) {
                    if (event[i].getAttribute("data-location") === locations[l]) {
                        matchFound = true;
                    }
                }
            } else if (locations.length === 0) {
                for (let t = 0; t < times.length; t++) {
                    for (let e = 0; e < expLevels.length; e++) {
                        if (event[i].getAttribute("data-time") === times[t] && event[i].getAttribute("data-exp") === expLevels[e]) {
                            matchFound = true;
                        }
                    }
                }
            } else if (times.length === 0) {
                for (let l = 0; l < locations.length; l++) {
                    for (let e = 0; e < expLevels.length; e++) {
                        if (event[i].getAttribute("data-location") === locations[l] && event[i].getAttribute("data-exp") === expLevels[e]) {
                            matchFound = true;
                        }
                    }
                }
            } else if (expLevels.length === 0) {
                for (let l = 0; l < locations.length; l++) {
                    for (let t = 0; t < times.length; t++) {
                        if (event[i].getAttribute("data-location") === locations[l] && event[i].getAttribute("data-time") === times[t]) {
                            matchFound = true;
                        }
                    }
                }
            }

            if (matchFound) {
                event[i].style.display = "grid";
            }
        }

        checkForNoMatches();
    }

    /*
    This function checks if any events are currently displayed. If they are, it adds them to the matchFound array. If the matchFound array is empty, it displays the no results message.
    */
    function checkForNoMatches() {
        const events = document.getElementsByClassName("event-card");
        let matchFound = [];

        for (let i = 0; i < events.length; i++) {
            if (events[i].style.display === "grid") {
                matchFound.push(events[i]);
                break;
            }
        }

        if (matchFound.length > 0) {
            document.getElementById("no-results").style.display = "none";
        } else {
            document.getElementById("no-results").style.display = "grid";
        }
    }
});