/* script that toggles the class of the HTML
tag HEADER to red (#FF0000) when the user clicks on
the tag DIV#toggle_header:
You can’t use document.querySelector
*/
const $ = window.$;
$('DIV#toggle_header').click(function () {
  $('HEADER').toggleClass('green red');
});
