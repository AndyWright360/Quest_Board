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

    // Function sourced from Code Institute Non-Relational Database TaskManager Project.
    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") == "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
});

/*
Performs a validation check on the text based event form inputs to ensure they contain characters.
Also, prevents a text input from starting or finishing with whitespace.
*/
document.getElementById("event-form").addEventListener("submit", function(event) {
    // Prevent form submission
    event.preventDefault();

    // Variables for text entry inputs
    let eventName = document.getElementById("event_name").value;
    let eventDescription = document.getElementById("description").value;

    // Check if only whitespace has been entered in either input
    if (eventName.trim() === '' || eventDescription.trim() === '' ) {
        alert("Inputs must not be empty");
        return;
    }

    // Check if either input starts or eb=nds with whitespace
    if (eventName.trim() != eventName || eventDescription.trim() != eventDescription) {
        alert("Inputs must not start or end with empty space");
        return;
    }

    // If all validations pass, submit the form
    event.target.submit();
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