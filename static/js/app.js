$(document).ready(function() {


	$("#existing-customer-container").hide();
 	$('#new-customer-radio').on("click", function() {
 		if($(this).is(':checked')) {
 			$("#existing-customer-container").show();
 		}
 	});

 	$('#query-existing-customer-btn').on('click', function() {
 		//Get value of fields
 		var cFirstName = $("#c-first-name").val().toLowerCase();
 		var cLastName = $("#c-last-name").val().toLowerCase();
 		
 		

 		$.ajax({
 			type: "get",
 			url: "http://localhost:8000/customers/get_customer/" + cFirstName + "/" + cLastName,
 		}).success(function(data) {
 			
 			if(!data.custom_fn) {
 				console.log(data);
 				$('.alert-msg').css("display", "block");
 			}
 			updateCustomerFormFields(data);
 		})
 		//Send ajax call to /customers/get_customer

 		//Query customer in customer view

 		//Return JSON of customer

 		//Append customer values to fields

 	});

 	$("#existing-vehicle").on("click", function() {
 		if($(this).is(':checked')) {
 			//Get vehicles
 		}
 	})

 	var updateCustomerFormFields = function(data) {
 		$("#id_first_name").val(data.customer_fn);
 		$("#id_middle_initial").val(data.customer_mi);
 		$("#id_last_name").val(data.customer_ln);
 		$("#id_email").val(data.customer_email);

 		$("#id_address").val(data.customer_address);


 	}
});


