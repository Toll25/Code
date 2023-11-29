export default function (exoplanetsService) {
    let operations = {
        GET: getExoplanets,
        POST
    };

    function getExoplanets(request, response, next) {
        response
            .status(200)
            .json(exoplanetsService.getExoplanets());
    };

    function POST(request, response, next) {};

    // NOTE: We could also use a YAML string here.
    getExoplanets.apiDoc = {
        summary: 'returns all exoplanets.',
        operationId: 'getExoplanets',
        parameters: [],
        responses: {
            200: {
                description: 'a list of exoplanets.',
                content: {
                    'application/json': {
                        schema: {
                            type: 'array',
                            items: {
                                $ref: '#/components/schemas/exoplanet'
                            }
                        }
                    },
                    'application/xml': {
                        schema: {
                            type: 'array',
                            items: {
                                $ref: '#/components/schemas/exoplanet'
                            }
                        }
                    }
                }
            },
            default: {
                description: 'An error occurred',
            }
        }
    };

    console.log(getExoplanets);

    return operations;
};