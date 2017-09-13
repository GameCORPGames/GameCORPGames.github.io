$(document).ready(function(){
    $("a").mouseenter(function(){
        $(this).fadeTo("slow", 0.5);
    });
	$("a").mouseleave(function(){
        $(this).fadeTo("slow", 1);
    });
});
