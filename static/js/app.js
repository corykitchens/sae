//
$(document).ready(function() {

	$('.btnSubmit').click(function() {
		$('form').submit();
	});

	$('.vehicle-list-select').hide();
	var vehicles;
 	$('#query-existing-customer-btn').on('click', function() {
 		var cFirstName = $("#c-first-name").val().toLowerCase();
 		var cLastName = $("#c-last-name").val().toLowerCase();
 		
 		

 		$.ajax({
 			type: "get",
 			url: "http://localhost:8000/customers/get_customer/" + cFirstName + "/" + cLastName,
 		}).success(function(data) {
 			if(data['msg']) {
 				console.log(data);
 				alert(data['msg']);
 			}
 			

 			updateCustomerFormFields(data);
 		})


 	});

 	var updateCustomerFormFields = function(data) {
 		
 		vehicles = JSON.parse(data['customer_vehicles']);
 		
 		$("#id_first_name").val(data.customer_fn);
 		$("#id_middle_initial").val(data.customer_mi);
 		$("#id_last_name").val(data.customer_ln);
 		$("#id_email").val(data.customer_email);

 		$("#id_address").val(data.customer_address);

 		for(var i = 0; i < vehicles.length; i++) {
 			var vehicle = vehicles[i].fields.year + " " + vehicles[i].fields.make + " " + vehicles[i].fields.model;
 			$('.vehicle-list-select').append("<option>" + vehicle + "</option>");
 		}
 		
 		$('.vehicle-list-select').show();
 		populateVehicleFields(vehicles[0]);
 	}

 	$('.vehicle-list-select').change(function() {
 	
 		var vehicleIndex = $(this).prop('selectedIndex');
 		populateVehicleFields(vehicles[vehicleIndex]);
 	});

 	var populateVehicleFields = function(selectedVehicle) {
 		$("#id_license_plate").val(selectedVehicle.fields.license_plate);
 		$("#id_make").val(selectedVehicle.fields.make);
 		$("#id_model").val(selectedVehicle.fields.model);
 		$("#id_vin").val(selectedVehicle.fields.vin);
 		$("#id_year").val(selectedVehicle.fields.year);
 		$("#vehicle_id").val(selectedVehicle.pk);
 		console.log($("#vehicle_id").val());
 	}
});


