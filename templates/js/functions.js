
$(document).ready(function() {

	$('.popup').css({ opacity: 0 });



	$('.form-container .search-field').focus(function() {
		/*
		if($(this).val() == "Type search text here...") {
			this.value = "";
		}
		*/
	});

	$('.form-container .search-field').keydown(function() {
		//$('.popup').css({ opacity: 0 });
	});

});


