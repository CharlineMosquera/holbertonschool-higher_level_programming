var addItemButton = document.getElementById('add_item');

addItemButton.addEventListener('click', function () {
    var newItem = document.createElement('li');

    newItem.textContent = 'Item';

    var myList = document.querySelector('.my_list');

    myList.appendChild(newItem);
});
