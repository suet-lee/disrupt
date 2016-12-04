$(document).ready(function(){

$('#alert-box input[type="submit"]').click(function(){
	ccode = $('#ccode').val();
	number = $('#pnum').val();
	area = $('#area').val();
	service = $('#service').val();
		console.log(ccode+number+area+service);
});

});
