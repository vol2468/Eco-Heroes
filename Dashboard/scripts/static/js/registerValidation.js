function handleFormSubmit(event) {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Retrieve username and city values from the form
    const username = document.getElementById("username").value.trim();
    const mycity = document.getElementById("selectedcity").value.trim();

    // Database query for the username and city validation
    
    

    // Store them in database
    
    // connection = sqlite3.connect('database.db')
    // cur = connection.cursor()
    // query = ("SELECT latitude, longitude, FROM city WHERE cname=%s")
    // latitude=
    // cur.execute("INSERT INTO kids (username, city, latitude, longitude) VALUES (?, ?, ?, ?)", (username, mycity, 0, 0))


    // Perform login validation
    if (username === "taii" && mycity !== "") {
        // Redirect to the index page (replace 'index.html' with the actual URL)
        window.location.href = "index";
    } else {
        // Display an error message (replace 'error-message' with the ID of your error message element)
        document.getElementById("error-message").textContent = "Please choose your city.";
    }
}

// Add event listener to the form submission event
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("login-form").addEventListener("submit", handleFormSubmit);
});