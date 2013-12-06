jQuery(document).ready(function($) {
	
//init
$('.menu').css({'opacity': 0, 'margin-top': -10});
		
//ROLLOVER
	$('.sezione').mouseenter(function() {
	var padre =	$(this).attr("ref");;
	$('.bg.'+padre).stop(true, true).animate({
		opacity: 0
		}, 500);
	$('.macrotit.'+padre).stop(true, true).animate({
		marginLeft: -10,
		opacity: 0
		}, 500);
	$('.menu.'+padre).stop(true, true).animate({
		opacity: 1,
		marginTop: 0
		}, 500);
	});

//ROLLOUT
	$('.sezione').mouseleave(function() {
	var padre =	$(this).attr("ref");;
	$('.bg.'+padre).stop(true, true).animate({
		opacity: 1
		}, 400);
	$('.macrotit.'+padre).stop(true, true).animate({
		marginLeft: 0,
		opacity: 1
		}, 500);
	$('.menu.'+padre).stop(true, true).animate({
		opacity: 0,
		marginTop: -10
		}, 500);
	});


});