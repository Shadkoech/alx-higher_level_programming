$(document).ready(function () {
  // Function adding  a new item to the list
  $('DIV#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });

  // Function removing the last item from the list
  $('DIV#remove_item').click(function () {
    $('ul.my_list li:last').remove();
  });

  // Function clearing  all items from the list
  $('DIV#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
