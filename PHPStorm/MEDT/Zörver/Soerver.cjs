const { exoplanetsModel } = require('./exoplanetsModel.cjs');
const express = require('express');
const app = express();
const port = 3000;

app.get('/exoplanets', (req, res) => {
    res.status(200).send(exoplanetsModel.exoplanets);
})

app.get('/exoplanets/:id', (req, res) => {
    const id = parseInt(req.params.id);
    res.status(200).send(exoplanetsModel.exoplanets.find((planet) => planet.id == id));
});

app.post('/exoplanets', (req, res) => {
    const exo = req.body;
    exoplanetsModel.exoplanets.push(exo);
    res.status(200).send('Added new exoplanet');
});

app.put('/exoplanets/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const updateExo = req.body;

    const indexOfChange = exoplanetsModel.exoplanets.findIndex((planet) => planet.id == id);

    if (indexOfChange == -1) {
        res.status(404).send('404 error: Exoplanet not found')
    } else {
        exoplanetsModel.exoplanets[indexOfChange] = {
            ...exoplanetsModel.exoplanets[indexOfChange], ...updateExo
        };

        res.status(200).send('Exoplanet updated');
    }
});

app.delete('/exoplanet/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const indexOfDel = exoplanetsModel.exoplanets.findIndex((planet) => planet.id == id);

    if (indexOfDel == -1) {
        res.status(202).send('404 error: exoplanet not found');
    } else {
        exoplanetsModel.exoplanets.slice(indexOfDel, 1);
        res.status(200).send('exoplanet deleted', exoplanets[id]);
    }
});

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
});