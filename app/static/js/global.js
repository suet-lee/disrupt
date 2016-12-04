$(document).ready(function(){

$('#alert-box i').click(function(){
	country_code = $('#ccode').val();
	phone_number = $('#pnum').val();
	area = $('#area').val();
	service = $('#service').val();
	var data = {"country_code": country_code, "phone_number": phone_number, "area": area, "service": service};
	$.post({"url": '/api/post-alert', "data": JSON.stringify(data), "contentType": "application/json"});
});

});
