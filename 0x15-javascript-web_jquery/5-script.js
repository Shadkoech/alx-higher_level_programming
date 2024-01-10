$(document).ready(function () {
  // Listening for a click event on the DIV#add_item
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
});
