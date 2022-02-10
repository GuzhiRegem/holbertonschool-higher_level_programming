$(document).ready(function() {
const lis = $('UL.my_list');
$('DIV#add_item').on('click', function(event) {
  lis.append('<li>Item</li>');
});
$('DIV#remove_item').on('click', function(event) {
  $('UL.my_list li').first().remove();
});
$('DIV#clear_list').on('click', function(event) {
  lis.empty();
});
});
