$(function() {
  // get current URL path and assign 'active' class
  var currentPath = location.pathname;
  $('.nav-link').each(function(){
    if($(this).attr('href') == currentPath) {
      $(this).addClass('active');
    }
  });

});
