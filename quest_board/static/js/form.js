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