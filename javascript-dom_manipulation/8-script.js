const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

fetch(apiUrl)
  .then(function (response) {
    if (response.ok) {
      return response.json();
    }
    throw new Error('Unable to obtain translation');
  })
  .then(function (data) {
    hello.textContent = data.hello;
  })
  .catch(function (error) {
    console.error('Error: ' + error.message);
  });
