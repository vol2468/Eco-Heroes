$(document).ready(function() {
    var myQuality = $("#airQ1").html();
    var othQuality = $("#airQ2").html();
    var winlose = $("#win-lose");

    if (myQuality > othQuality) {
        winlose.html("You win!");
        var congrats = $('<script>confetti({particleCount: 100, spread: 70, origin: { y: 0.6 }});</script>');
        $("body").append(congrats);
    } else if (myQuality < othQuality) {
        winlose.html("You lose...");
        $("#win-lose").css("color", "navy");
    } else {
        winlose.html("Almost! It's a draw.")
    }
});