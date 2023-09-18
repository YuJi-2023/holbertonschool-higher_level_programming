$(function () {
  $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    let movie_list = data.results;

    //iterate over the list to get each title
    $.each(movie_list, function (index, movie) {
      $("UL#list_movies").append("<li>" + movie.title + "</li>");
    })
  })
})