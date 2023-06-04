document.getElementById('recipe-form').addEventListener('submit', function(event) {
    event.preventDefault();

    var dishname = document.getElementById('dish_name').value;

    fetch('/generate_recipe', {
        method: 'POST',
        body: new URLSearchParams('dish_name=' + dishname),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('recipe').textContent = data;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
