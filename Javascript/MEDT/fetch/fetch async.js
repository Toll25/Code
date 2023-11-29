async function fetchData() {
    const url = 'http://localhost:3000/exoplanets';
    try {
        const response = await fetch(url);

        const data = await response.json();
        console.log(data);
    } catch (ex) {
        console.error(ex)
    }
}

fetchData()