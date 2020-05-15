/* script that adds a LI element to a list
when the user clicks on the tag DIV#add_item:
You can’t use document.querySelector to select the HTML tag
*/
const $ = window.$;
$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
