#!/usr/local/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';

const getCharacterNames = (filmUrl) => {
  return new Promise((resolve, reject) => {
    request(filmUrl, (error, response, body) => {
      if (error) {
        reject(new Error('Request error: ' + error));
      } else {
        try {
          const filmData = JSON.parse(body);
          const characterUrls = filmData.characters;
          resolve(characterUrls);
        } catch (e) {
          reject(new Error('Error parsing JSON: ' + e.message));
        }
      }
    });
  });
};

const getCharacterName = (characterUrl) => {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(new Error('Request error: ' + error));
      } else {
        try {
          const characterData = JSON.parse(body);
          resolve(characterData.name);
        } catch (e) {
          reject(new Error('Error parsing JSON: ' + e.message));
        }
      }
    });
  });
};

// Construct the correct film URL
const filmUrl = `${apiUrl}${movieId}/`;

getCharacterNames(filmUrl)
  .then(characterUrls => {
    return Promise.all(characterUrls.map(url => getCharacterName(url)));
  })
  .then(characterNames => {
    characterNames.forEach(name => console.log(name));
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
