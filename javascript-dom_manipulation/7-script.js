const listMoviesElement = document.getElementById('list_movies');

const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(apiUrl)
  .then(function (response) {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error('The list of films could not be obtained');
    }
  })
  .then(function (data) {
    const movies = data.results;

    movies.forEach(function (movie) {
      const title = movie.title;
      const listItem = document.createElement('li');
      listItem.textContent = title;
      listMoviesElement.appendChild(listItem);
    });
  })
  .catch(function (error) {
    console.error('Error: ' + error.message);
  });
