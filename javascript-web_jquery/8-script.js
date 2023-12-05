#!/usr/bin/node

$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    const movies = data.results;
    const listMovies = $('#list_movies');

    movies.forEach(function (movie) {
      listMovies.append('<li>' + movie.title + '</li>');
    });
  });
});
