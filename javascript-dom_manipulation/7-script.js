var listMoviesElement = document.getElementById('list_movies');

var apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(apiUrl)
    .then(function (response) {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('The list of films could not be obtained');
        }
    })
    .then(function (data) {
        var movies = data.results;

        movies.forEach(function (movie) {
            var title = movie.title;
            var listItem = document.createElement('li');
            listItem.textContent = title;
            listMoviesElement.appendChild(listItem);
        });
    })
    .catch(function (error) {
        console.error('Error: ' + error.message);
    });
