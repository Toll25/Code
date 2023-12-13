import {exoplanetsModel} from "../models/exoplanetsModel.js";

export default function (exoplanetsService) {
    let operations = {
        GET: getExoplanets,
        POST: createExoplanet,
    };

    async function getExoplanets(request, response, next) {
        response
            .status(200)
            .json(await exoplanetsService.getExoplanets());
    };

    function createExoplanet(request, response, next) {
        exoplanetsModel.exoplanets.push(request.body)
        response.status(200).json("Added new Exoplanet")
    };

    createExoplanet.apiDoc = {
        summary: 'adds a Exoplanet.',
        operationId: 'createExoplanet',
        parameters: [],
        requestBody: {
            content: {
                'application/json': {
                    schema: {
                        $ref: '#/components/schemas/exoplanet'
                    }
                }
            }
        },
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