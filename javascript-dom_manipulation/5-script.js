const updateHeader = document.getElementById('update_header');

updateHeader.addEventListener('click', function () {
  const headerElement = document.querySelector('header');

  headerElement.textContent = 'New Header!!!';
});
