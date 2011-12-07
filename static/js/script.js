$(document).ready(function() {
  $("a[rel=zoom]").fancybox({
    'titlePosition' 	: 'outside',
    'titleFormat'	: function(title, currentArray, currentIndex, currentOpts) {
	return '<span id="fancybox-title-over">Image ' + (currentIndex + 1) + ' / ' + currentArray.length + (title.length ? ' &nbsp; ' + title : '') + '</span>';}
  });
});

$('button#b-all').bind('click', function(event) {
  $.cookie("nobred", 1);
  $('button#b-all').attr("disabled", true);
  $('button#b-nobred').removeAttr("disabled");
  //return false;
});

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
