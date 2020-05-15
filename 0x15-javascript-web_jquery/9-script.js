/* script that fetches from `https://fourtonfish.com/hellosalut/?lang=fr` and
displays the value of hello from that fetch in the HTML’s tag DIV#hello.
You can’t use document.querySelector to select the HTML tag
 */
const $ = window.$;
$(document).ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr',
    function (data) {
      $('DIV#hello').text(data.hello);
    }
  );
});
