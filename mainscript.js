var wHeight = $(window).height();
var wWidth = $(window).width();
var pWide = wWidth / 20;
var pHeader = "1em " + pWide + "px" + " 1em " + pWide + "px";
$(document).ready(function(){
    $("#header-links").css("padding", pHeader);
    $("a").mouseenter(function(){
        $(this).fadeTo("slow", 0.5);
    });
    $("a").mouseleave(function(){
        $(this).fadeTo("slow", 1);
    });
});

