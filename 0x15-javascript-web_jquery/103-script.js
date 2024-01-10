$(document).ready(function () {
  // Fetching the user input  and display the translation
  function fetchTranslation () {
    const languageCode = $('INPUT#language_code').val();

    // Making  AJAX request to the API to fetch the translation
    $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode })
      .done(function (response) {
        // Display the translation in the HTML tag DIV#hello
        $('DIV#hello').text(response.hello);
      });
  }

  // Event handler for button click
  $('INPUT#btn_translate').click(function () {
    fetchTranslation();
  });

  // Event handler for ENTER key press on INPUT#language_code
  // 13 is the key code for ENTER
  $('INPUT#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
});
