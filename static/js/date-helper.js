var expired = false
// reg length
var regLength = parseInt($('#lengthOfReg').text().substring(0,1));

// get reg date
var dateString = $('#dateOfReg').text();
var regMonth = parseInt(dateString.substr(5,2));
var regDay = parseInt(dateString.substr(8,2));
var regYear = parseInt(dateString.substr(0,4));
$('#dateOfReg').text($('#dateOfReg').text().substr(0,10));
// get todays date
var today = new Date();
var day = today.getDate();
var month = today.getMonth()+1;
var year = parseInt(today.getFullYear());
if(day < 10){
  day = parseInt('0'+day);
}
if(month < 10){
  month = parseInt('0'+month);
}

if(year >= (regYear + regLength)){
  if(month >= regMonth){
    if(day >= regDay){
      expired = true
    }
  }
}

if(expired){
  $('#expired').text('EXPIRED');
}
else{
  $('#expired').text('ACTIVE');
}