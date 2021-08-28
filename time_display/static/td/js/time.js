showDate();
showTime();

function showTime(){
var myDate = new Date();
var hours = myDate.getHours();
var minutes = myDate.getMinutes();
var seconds = myDate.getSeconds();
if (hours < 10) hours = 0 + hours;
if (minutes < 10) minutes = "0" + minutes;
if (seconds < 10) seconds = "0" + seconds;
$("#HoraActual").text(hours+ ":" +minutes+ ":" +seconds);
setTimeout("showTime()", 1000);
}

function showDate(){
	var months = new Array ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre");
	var myDate = new Date();
	$("#Fecha").text(months[myDate.getMonth()] + " " + myDate.getDate() + ", " +myDate.getFullYear());
	setTimeout("showDate()", 1000);
	}
	