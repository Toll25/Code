const apiDoc = {
    openapi: '3.1.0',
    info: {
        title: 'api for discovered exoplanets.',
        version: '1.0.0'
    },
    servers: [
        {
            url: 'http://localhost:8000/api/v1',
            description: 'local development server'
        }
    ],
    components: {
        schemas: {
            exoplanet: {
                type: 'object',
                properties: {
                    id: {
                        description: 'id of the exoplanet.',
                        type: 'number'
                    },
                    planet_name: {
                        description: 'name of the exoplanet.',
                        type: 'string'
                    },
                    hostname: {
                        description: `name of the exoplanet's host.`,
                        type: 'string'
                    },
                    planet_letter: {
                        description: 'letter for the exoplanet (first planet next to host = a, ...).',
                        type: 'string'
                    },

                },
                required: ['id', 'planet_name', 'hostname']
            }
        }
    },
    paths: {}
};

export default apiDoc;