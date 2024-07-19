#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/';

const getCharacterNames = (filmUrl) => {
  return new Promise((resolve, reject) => {
    request(filmUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const filmData = JSON.parse(body);
        const characterUrls = filmData.characters;
        resolve(characterUrls);
      }
    });
  });
};

const getCharacterName = (characterUrl) => {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      }
    });
  });
};

getCharacterNames(apiUrl + 'films/' + movieId)
  .then(characterUrls => {
    return Promise.all(characterUrls.map(url => getCharacterName(url)));
  })
  .then(characterNames => {
    characterNames.forEach(name => console.log(name));
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
