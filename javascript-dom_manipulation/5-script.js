var updateHeader = document.getElementById('update_header');

updateHeader.addEventListener('click', function () {
    var headerElement = document.querySelector('header');

    headerElement.textContent = 'New Header!!!';
});
