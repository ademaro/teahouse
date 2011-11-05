//$(document).ready(function() {
  
//});

$('a.expand').bind('click', function(event) {
  var ttt = $(this).text();
  if (ttt == 'Развернуть'){
     $(this).text('Свернуть');
   
  } else {
     $(this).text('Развернуть');
  }
  $(this).parent().next().stop(true, true).fadeToggle();
  return false;
});

$("a.expand").bind("dblclick", function(){
  //$(this).parent.next().stop();
  //$(this).text('qwe');
  window.location.href = $(this).attr('href');
});
