$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    // capture the language code entered by the user
    const languageCode = $('INPUT#language_code').val();

    // Making AJAX request to the API to fetch the translation
    $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode })
      .done(function (response) {
        // Display the translation in the HTML tag DIV#hello
        $('DIV#hello').text(response.hello);
      });
  });
});
