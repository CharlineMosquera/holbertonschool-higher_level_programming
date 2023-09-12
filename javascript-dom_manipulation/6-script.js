const characterElement = document.getElementById('character');

const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(apiUrl)
  .then(function (response) {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error('Error');
    }
  })
  .then(function (data) {
    const characterName = data.name;

    characterElement.textContent = characterName;
  })
  .catch(function (error) {
    console.error('Error: ' + error.message);
  });
