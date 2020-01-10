"""Route-related configuration."""

import json

from . import handlers


def setup_routes(app,
                 debug=False,
                 app_prefix="etda",
                 api_prefix='api',
                 ver_prefix='v1'):
    """Set up routes according to {app}/api/v{ver}/{resource}.

    Arguments:

    app_prefix: Application prefix. Default: main package name
    api_prefix: API prefix. Default: "api"
    ver_prefix: Version prefix. Default: v1
    """
    prefix = f'/{app_prefix}/{api_prefix}/{ver_prefix}'
    app.router.add_post(f'{prefix}/status', handlers.status_check)
