var characterElement = document.getElementById('character');

var apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(apiUrl)
    .then(function (response) {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Error');
        }
    })
    .then(function (data) {
        var characterName = data.name;

        characterElement.textContent = characterName;
    })
    .catch(function (error) {
        console.error('Error: ' + error.message);
    });
