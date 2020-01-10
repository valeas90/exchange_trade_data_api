from aiohttp.web import json_response


async def status(request):
    """Status check.

    Implement here all your app's needs to be considered "alive".
    This is the endpoint to be exposed as test for load balancing.

    By default, if the app can response to this same call with
    any json response, it will be considered alive.

    ---
    description: Status check.
    tags:
    - Health check
    parameters:
      - in: body
        name: body
        description: Status request data
        schema:
          type: object
          properties:
            curdate:
              type: number
          required:
            - curdate
    produces:
    - application/json
    responses:
        "200":
            description: All systems OK.
        "500":
            description: Not ok

    """
    response = {'status': 200}
    return json_response(response)
