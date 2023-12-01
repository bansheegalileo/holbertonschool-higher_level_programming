#!/usr/bin/node

const request = require('request');

function getStarWarsMovieTitle (movieId) {
  const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
      return;
    }

    const movieData = JSON.parse(body);
    const { title, episode_id } = movieData;
    console.log(`Episode ${episode_id}: ${title}`);
  });
}

const args = process.argv.slice(2);

if (args.length !== 1) {
  console.error('Usage: node script.js <movie_id>');
  process.exit(1);
}

const movieId = args[0];
getStarWarsMovieTitle(movieId);
