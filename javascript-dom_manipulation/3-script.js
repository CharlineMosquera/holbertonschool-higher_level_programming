const headerElement = document.querySelector('header');

const toggleHeader = document.getElementById('toggle_header');

toggleHeader.addEventListener('click', function () {
  if (headerElement.classList.contains('red')) {
    headerElement.classList.remove('red');
    headerElement.classList.add('green');
  } else {
    headerElement.classList.remove('green');
    headerElement.classList.add('red');
  }
});
