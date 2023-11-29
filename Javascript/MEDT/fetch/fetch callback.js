function fetchData() {
    const url = 'http://localhost:3000/exoplanets';
    fetch(url)
        .then(response => {
            return response.json();
        })
        .then(data => {
            console.log(data);
        })
        .then(ex => {
            console.error(ex);
        });
}

fetchData()