//
$(document).ready(function() {


	// Generate Customer Report
	$('#reportBtn').click(function() {
		console.log('Hello world');
		generateCustomerReport();
	});


	// Submit Work Order
	$('.btnSubmit').click(function() {
		if (verifyInput()) {
			$('form').submit();
		}
		
	});

	// Service Notes
	$('.submit-note').click(function() {
		submitNote();
		$('form').trigger('reset');
	});

	// Payment Processing
	$('#submitPayment').click(function() {
		processPayment();
	})
	$('.vehicle-list-select').hide();
	var vehicles;
 	$('#query-existing-customer-btn').on('click', function() {
 		var cFirstName = $("#c-first-name").val().toLowerCase();
 		var cLastName = $("#c-last-name").val().toLowerCase();
 		
 		

 		$.ajax({
 			type: "get",
 			url: "/customers/get_customer/" + cFirstName + "/" + cLastName,
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
 		$("#vehicle_id").val(-1);
 		
 		for(var i = 0; i < vehicles.length; i++) {
 			var vehicle = vehicles[i].fields.year + " " + vehicles[i].fields.make + " " + vehicles[i].fields.model;
 			$('.vehicle-list-select').append("<option>" + vehicle + "</option>");
 		}
 		
 		$('.vehicle-list-select').show();
 		//populateVehicleFields(vehicles[0]);
 	}

 	$('.vehicle-list-select').change(function() {
 	
 		var vehicleIndex = $(this).prop('selectedIndex');
 		console.log(vehicleIndex);
 		if(vehicleIndex > 0) {
 			populateVehicleFields(vehicles[vehicleIndex-1]);
 		} else {
 			console.log('inside clear');
 			$('.vehicle-information-fields').find('input').val('');
 		}

 		
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

var checkCurrentLocation = function() {
	var loc = document.location.pathname;
	console.log(loc);
	
}


var submitNote = function() {

	//Time
	var time_spent = $('#time-spent').val();
	// //Notes
	var notes_text = $('#service-notes').val();
	// //Parts
	var parts = []
	$('#parts-selected > option:selected').each(function() {
		parts.push(this.value);
	});
	console.log(parts);

	// //Status
	var status = $('#service-status').val();
	// //Reassigning?
	console.log(status);
	var work_order_id = $('#work_order_id').val();
	
	var reassign_status = $("#reassign").val();

	$.ajax({
		url : '/workorders/submit_service_notes/',
		type : 'get',
		data : {
			'id' : work_order_id,
			'time_spent' : time_spent,
			'notes' : notes_text,
			'parts_list' : JSON.stringify(parts),
			'status' : status,
			'reassign' : reassign_status
		}
	}).success(function(data) {
		updateNotesTable(data);
	});

}


var updateNotesTable = function(data) {
	//Update Tech
	console.log(data['date']);
	var row = $("<tr>");
	row.append($("<td>").text(data['emp']));
	row.append($("<td>").text(data['date']));
	row.append($("<td>").text(data['time_spent']));
	row.append($("<td>").text(data['notes']));
	row.append($("<td>").text(data['parts']));
	// //Start new record
	$(".emp-notes:last-child").append(row);
	

}


var verifyInput = function() {
	
	if (($('#id_service_type').prop("selectedIndex") == -1)) {
		$("#id_service_type").addClass("alert alert-danger");
		$("#id_service_type").css("border", "1px solid red");
		return false;
	} else {
		return true;
	}
	
}

var generateCustomerReport = function() {
	
	var data = [
	{
		value: 500,
		color: "#52409AB",
		label: "A"
	},
	{
		value: 250,
		color: "#5AX09AB",
		label: "B"
	},
	
	]

	var ctx = document.getElementById("myChart").getContext("2d");
	var myNewChart = new Chart(ctx).PolarArea(data);
	

}

var processPayment = function() {
	var est_init = $("#e_initial").val();
	var final_cost = $("#e_final").val();
	var payment_amount = $("#payment_amount").val();
	var w_id = $("#w_id").val();
	var csrftoken = $.cookie("csrftoken");
	console.log(payment_amount)

	$.ajax({
		url : '/workorders/process_payment/' + w_id + "/",
		type : 'post',
		data : {
			'csrfmiddlewaretoken' : csrftoken,
			'work_order_id' : w_id,
			'estimate_initial': est_init,
			'final_cost' : final_cost,
			'payment_amount' : payment_amount,
		}
	}).success(function(data) {
		$('#myModal').modal('show');
	}).error(function(data) {
		console.log(data['responseText']);
	})

}

























