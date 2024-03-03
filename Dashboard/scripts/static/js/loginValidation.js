function handleFormSubmit(event) {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Retrieve username and city values from the form
    const username = document.getElementById("username").value.trim();

    // Database query for the username validation
    


    // Perform login validation
    if (username === "taii") {
        // Redirect to the index page (replace 'index.html' with the actual URL)
        window.location.href = "index";
    } else {
        // Display an error message (replace 'error-message' with the ID of your error message element)
        document.getElementById("error-message").textContent = "Please enter your username.";
    }
}

// Add event listener to the form submission event
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("login-form").addEventListener("submit", handleFormSubmit);
});