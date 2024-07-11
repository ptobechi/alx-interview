#!/usr/bin/node

const axios = require('axios');

const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/';

axios.get(apiUrl + 'films/' + movieId)
  .then(response => {
    const charactersUrls = response.data.characters;
    return Promise.all(charactersUrls.map(url => axios.get(url)));
  })
  .then(charactersResponses => {
    const characterNames = charactersResponses.map(response => response.data.name);
    characterNames.forEach(name => console.log(name));
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
