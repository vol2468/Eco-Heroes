$(document).ready(function() {
    var myQuality = $("#airQ1").html();
    var othQuality = $("#airQ2").html();
    var winlose = $("#win-lose");

    if (myQuality > othQuality) {
        winlose.html("You won!");
    } else if (myQuality < othQuality) {
        winlose.html("You lost...");
    } else {
        winlose.html("Almost! It's a draw.")
    }
});