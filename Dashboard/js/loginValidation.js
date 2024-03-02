function handleFormSubmit(event) {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Retrieve username and city values from the form
    const username = document.getElementById("username").value;
    const mycity = document.getElementById("mycity").value;

    // Perform login validation
    if (username.trim() === "taii" && mycity.trim() === "kelowna") {
        // Redirect to the index page (replace 'index.html' with the actual URL)
        window.location.href = "../templates/index.html";
    } else {
        // Display an error message (replace 'error-message' with the ID of your error message element)
        document.getElementById("error-message").textContent = "Invalid username or city. Please try again.";
    }
}

// Add event listener to the form submission event
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("login-form").addEventListener("submit", handleFormSubmit);
});
