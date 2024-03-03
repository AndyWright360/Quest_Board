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
    $('.datepicker').datepicker({
        format: "dd mmm, yyyy"
    });

    // Initialise character counter for forms
    $('input#event_name, textarea#description').characterCounter();

    // Initialise collapsible
    $('.collapsible').collapsible();

    // Initialise modal
    $('.modal').modal();

    // Sets an auto timer to scroll to the next slide for the carousel.
    autoplay();
    function autoplay() {
        $('.carousel').carousel('next');
        setTimeout(autoplay, 5000);
    };
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
