#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  const actors = data.actors;

  for (const actor of actors) {
    request(actor, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const actorData = JSON.parse(body);
      console.log(actorData.name);
    });
  }
});
