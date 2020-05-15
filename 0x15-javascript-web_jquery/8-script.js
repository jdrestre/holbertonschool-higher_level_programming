/* script that fetches and lists all movies title by using
this URL: `https://swapi-api.hbtn.io/api/films/?format=json`
You can’t use document.querySelector to select the HTML tag
*/
const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
});
