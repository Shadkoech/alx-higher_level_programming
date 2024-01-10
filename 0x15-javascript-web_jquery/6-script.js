$(document).ready(function () {
  // Listening for a click event on the DIV#update_header
  $('DIV#update_header').click(function () {
    $('header').text('<New Header!!!');
  });
});
