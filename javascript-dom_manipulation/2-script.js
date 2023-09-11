var redHeader = document.getElementById('red_header');

redHeader.addEventListener('click', function () {
    var header = document.querySelector('header');

    header.classList.add('red');
});
