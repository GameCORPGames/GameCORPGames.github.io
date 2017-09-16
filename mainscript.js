var wHeight = $(window).height();
var wWidth = $(window).width();
var pWide = wWidth / 20;
$(document).ready(function(){
    $("#header-links").css("padding", "1em " + pWide + " 1em " + pWide);
    $("a").mouseenter(function(){
        $(this).fadeTo("slow", 0.5);
    });
    $("a").mouseleave(function(){
        $(this).fadeTo("slow", 1);
    });
});
alert("padding", "1em " + pWide + " 1em " + pWide);
