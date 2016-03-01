$(document).ready(function() {


	$("#existing-customer-container").hide();
 	$('#existing-customer-radio').on("click", function() {
 		if($(this).is(':checked')) {
 			$("#existing-customer-container").show();
 		}
 	});

 	$('#new-customer-radio').on("click", function() {
 		console.log('test');
 		$("#existing-customer-container").hide();
 	});

 	$("#existing-vehicle").on("click", function() {
 		if($(this).is(':checked')) {
 			$("existing-vehicle-container").show();
 		}
 	})

 	$('#query-existing-customer-btn').on('click', function() {
 		//Get value of fields
 		var cFirstName = $("#c-first-name").val().toLowerCase();
 		var cLastName = $("#c-last-name").val().toLowerCase();
 		
 		

 		$.ajax({
 			type: "get",
 			url: "http://localhost:8000/customers/get_customer/" + cFirstName + "/" + cLastName,
 		}).success(function(data) {
 			console.log(data);
 			if(data['msg']) {
 				console.log(data);
 				$('.alert-msg').css("display", "block");
 			}
 			console.log(data);

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

 		//TODO, refactor for dynamically adding vehicles
 		$("#existing-vehicle-list").append("<option>" + data['vehicle0'] + "</option>");
 		$("#existing-vehicle-list").append("<option>" + data['vehicle1'] + "</option>");
 		$("#existing-vehicle-list").append("<option>" + data['vehicle2'] + "</option>");
 		$("#existing-vehicle-list").append("<option>" + data['vehicle3'] + "</option>");


 	}

 	$("#existing-vehicle-list").change(function() {
 		console.log('Worked');
 		
 		
 	});
});


