$(document).ready(function () {
  // Listening for a click event on the DIV#red_header
  $('#red_header').click(function () {
    // Selecting <header> element and updating its text color to red
    $('header').css('color', '#FF0000');
  });
});
