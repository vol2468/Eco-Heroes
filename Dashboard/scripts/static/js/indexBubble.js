$(document).ready(function() {
    var globe = $("#globe");
    var bubble = $("#start");

    globe.mouseenter(function() {
        bubble.css({
            "animation-name": "expand-bounce",
            "animation-duration": "0.25s"
        });
    }).mouseleave(function() {
        bubble.css({
            "animation-name": "shrink",
            "animation-duration": "0.1s"
        });
    });
});
