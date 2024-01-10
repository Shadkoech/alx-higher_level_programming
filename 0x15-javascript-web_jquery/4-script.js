$(document).ready(function () {
  // Listening for a click event on the DIV#toggle_header
  $('DIV#toggle_header').click(function () {
    $('header').toggleClass('green red');
  });
});
