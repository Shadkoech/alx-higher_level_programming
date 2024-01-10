$(document).ready(function () {
  // Using AJAX method $.get to fetch data from the SWAPI API
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    // Displaying the character name in the HTML tag DIV#character
    $('DIV#character').text(data.name);
  });
});
