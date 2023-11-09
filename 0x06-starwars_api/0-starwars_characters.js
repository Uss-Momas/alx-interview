#!/usr/bin/node
// starwars api calls
const request = require('request');

const apiUrl = 'https://swapi-api.alx-tools.com/api/films';

const argv = process.argv;

request.get(`${apiUrl}/${argv[2]}`, (err, resp, body) => {
  if (err) throw err;
  const movie = JSON.parse(body);
  const peoples = movie.characters;

  // start point for getting peoples name
  getPeople(peoples, 0);
});

function getPeople (peoples, position) {
  // condition of stopping
  if (position === peoples.length) return;

  request.get(peoples[position], (err, resp, body) => {
    if (err) throw err;

    const people = JSON.parse(body);
    console.log(people.name);
    // get the next actor name
    getPeople(peoples, position + 1);
  });
}
