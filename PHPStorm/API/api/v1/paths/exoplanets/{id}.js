import {exoplanetsModel} from "../../models/exoplanetsModel.js";

export default function (exoplanetsService) {
    let operations = {
        GET: getById,
        PUT,
        DELETE
    };

    function getById(request, response, next) {
        const exoplanet = exoplanetsModel.exoplanets.find(x => x.id == request.params.id);
        if (exoplanet !== undefined) {
            response
                .status(200)
                .json(exoplanet);
        } else {
            response.sendStatus(404);
        }
    };

    function PUT(request, response, next) {
    };

    function DELETE(request, response, next) {
    };

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

    return operations;
};