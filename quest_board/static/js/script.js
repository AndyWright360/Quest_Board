$(document).ready(function () {

    // Initialise side navbar
    $('.sidenav').sidenav();

    // Initialise carousel
    $('.carousel.carousel-slider').carousel({
        fullWidth: true,
        indicators: true
    });

    // Initialise form select
    $('select').formSelect();

    // Initialise datepicker
    $('.datepicker').datepicker();

    // Initialise character counter for forms
    $('input#event_name, textarea#description').characterCounter();

    // Initialise collapsible
    $('.collapsible').collapsible();
});

// Create variable of footer icons
const icons = document.getElementsByClassName("footer-icon");

// Add the grow style class to target
const grow = function () {
    this.classList.add("grow");
};

// Remove the grow style class from target
const shrink = function () {
    this.classList.remove("grow");
};

// Loop through footer icons to apply event listeners
for (let i = 0; i < icons.length; i++) {
    icons[i].addEventListener("mouseenter", grow);
    icons[i].addEventListener("mouseleave", shrink);
};
