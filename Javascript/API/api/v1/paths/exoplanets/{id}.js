import {exoplanetsModel, getExoplanetById} from "../../models/exoplanetsModel.js";

export default function (exoplanetsService) {
    let operations = {
        GET: getById,
        PUT: replaceById,
        PATCH: updateById,
        DELETE: deleteById
    };

    async function getById(request, response, next) {
        response
            .status(200)
            .json(await getExoplanetById(request.params.id));
        
    }

    function replaceById(request, response, next) {
        let exoplanetIndex = exoplanetsModel.exoplanets.findIndex(x => x.id === request.params.id);
        if (exoplanetIndex !== -1) {
            exoplanetsModel.exoplanets[exoplanetIndex] = request.body;

            response
                .status(200)
                .json(request.body);
        } else {
            response.sendStatus(404);
        }
    }

    function updateById(request, response, next) {
        let exoplanetIndex = exoplanetsModel.exoplanets.findIndex(x => x.id === request.params.id);
        if (exoplanetIndex !== -1) {
            exoplanetsModel.exoplanets[exoplanetIndex] = {
                ...exoplanetsModel.exoplanets[exoplanetIndex],
                ...request.body
            };

            response
                .status(200)
                .json(request.body);
        } else {
            response.sendStatus(404);
        }
    }

    function deleteById(request, response, next) {
        const exoplanetIndex = exoplanetsModel.exoplanets.findIndex(x => x.id === request.params.id);
        if (exoplanetIndex !== -1) {
            exoplanetsModel.exoplanets.splice(exoplanetIndex, 1);

            response
                .status(200)
                .json(request.body);
        } else {
            response.sendStatus(404);
        }
    }

    getById.apiDoc = {
        summary: 'returns a single exoplanet by id.',
        operationId: 'getExoplanetById',
        parameters: [
            {
                name: 'id',
                in: 'path',
                description: 'id of exoplanet to return.',
                required: true,
                schema: {
                    type: 'integer',
                    format: 'int64'
                }
            }
        ],
        responses: {
            200: {
                description: 'an exoplanet with the given id.',
                content: {
                    'application/json': {
                        schema: {
                            $ref: '#/components/schemas/exoplanet'
                        }
                    },
                    'application/xml': {
                        schema: {
                            $ref: '#/components/schemas/exoplanet'
                        }
                    }
                }
            },
            404: {
                description: 'exoplanet with given id does not exist.'
            }
        }
    };

    replaceById.apiDoc = {
        summary: 'replaces a single exoplanet by id.',
        operationId: 'replaceById',
        parameters: [
            {
                name: 'id',
                in: 'path',
                description: 'id of exoplanet to replace.',
                required: true,
                schema: {
                    type: 'integer',
                    format: 'int64'
                }
            }
        ],
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
                description: 'the replaced exoplanet.',
                content: {
                    'application/json': {
                        schema: {
                            $ref: '#/components/schemas/exoplanet'
                        }
                    },
                    'application/xml': {
                        schema: {
                            $ref: '#/components/schemas/exoplanet'
                        }
                    }
                }
            },
            404: {
                description: 'exoplanet with given id does not exist.'
            }
        }
    };

    updateById.apiDoc = {
        summary: 'updates a single exoplanet by id.',
        operationId: 'updateById',
        parameters: [
            {
                name: 'id',
                in: 'path',
                description: 'id of exoplanet to update.',
                required: true,
                schema: {
                    type: 'integer',
                    format: 'int64'
                }
            }
        ],
        requestBody: {
            content: {
                'application/json': {
                    schema: {
                        type: 'object',
                        properties: {
                            planet_name: {
                                type: 'string'
                            },
                            hostname: {
                                type: 'string'
                            },
                            planet_letter: {
                                type: 'string'
                            }
                        },
                    }
                }
            }
        },
        responses: {
            200: {
                description: 'the updated exoplanet.',
                content: {
                    'application/json': {
                        schema: {
                            $ref: '#/components/schemas/exoplanet'
                        }
                    },
                    'application/xml': {
                        schema: {
                            $ref: '#/components/schemas/exoplanet'
                        }
                    }
                }
            },
            404: {
                description: 'exoplanet with given id does not exist.'
            }
        }
    };

    deleteById.apiDoc = {
        summary: 'deletes a single exoplanet by id.',
        operationId: 'deleteById',
        parameters: [
            {
                name: 'id',
                in: 'path',
                description: 'id of exoplanet to delete.',
                required: true,
                schema: {
                    type: 'integer',
                    format: 'int64'
                }
            }
        ],
        responses: {
            200: {
                description: 'the deleted exoplanet.',
                content: {
                    'application/json': {
                        schema: {
                            $ref: '#/components/schemas/exoplanet'
                        }
                    },
                    'application/xml': {
                        schema: {
                            $ref: '#/components/schemas/exoplanet'
                        }
                    }
                }
            },
            404: {
                description: 'exoplanet with given id does not exist.'
            }
        }
    };

    return operations;
}