$(document).ready(function() {
  const url = 'https://www.fourtonfish.com/hellosalut/?lang=';
  const func = function(event) {
    const code = $('INPUT#language_code').val();
    $.get(url + code, function(data) {
      $('DIV#hello').text(data.hello)
    });
  };
  $('INPUT#btn_translate').on('click', func);
  $('INPUT#language_code').keydown(function(e) {
    if (event.which == 13) {
      func();
    }
  });
});
