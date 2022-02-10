$(document).ready(function() {
  const url = 'https://www.fourtonfish.com/hellosalut/?lang=';
  $('INPUT#btn_translate').on('click', function(event){
    const code = $('INPUT#language_code').val();
    $.get(url + code, function(data) {
      $('DIV#hello').text(data.hello)
    });
  });
});
