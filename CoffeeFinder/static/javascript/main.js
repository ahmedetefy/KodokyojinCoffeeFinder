
$(document).ready(function(){
	$('#order_form').submit(function(event){
				$("#successMessage").hide();
				$("#errorMessage").hide();

		event.preventDefault();
		$.ajax({
			url: $('#order_form').attr('action'),
			type: "POST",
			data: $('#order_form').serialize(),
			success: function(response){
				if (response == "error")
					$("#errorMessage").show();
				else  {
					$("#successMessage").show();
				}

			},
			error: function(response){
				$("#errorMessage").show();
			},
		})
	})
})
