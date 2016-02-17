$(document).ready(function() {
	$('.new-customer-form').hide();
	$('.existing-customer-form').hide();
	//getActiveLink();
 
	$("#new-customer-select").on("click", function() {
		if($(this).is(':checked')) {
			$('.new-customer-form').show(1000);
		}
	});

	$("#existing-customer-select").on("click", function() {
		if($(this).is(':checked')) {
			$('.existing-customer-form').show(1000);
		}
	})

	var appendNewCustomerElements = function() {

	}
});


var getActiveLink = function() {

	var currentPath = window.location.pathname;
	//Get path
	//Compare path to href
	console.log($(".side-nav").size());
	//append css class

}