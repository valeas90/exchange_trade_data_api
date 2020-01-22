"""Route-related configuration."""

import json

from exchange_trade_data_api.handlers.status import status_check
from exchange_trade_data_api.handlers.trades import trades_get
from exchange_trade_data_api.handlers.trades import trade_post
from exchange_trade_data_api.handlers.trades import trade_get
from exchange_trade_data_api.handlers.trades import trade_put
from exchange_trade_data_api.handlers.trades import trade_delete


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
    pub_prefix = f'/{app_prefix}/{api_prefix}/{ver_prefix}'
    app.router.add_post(f'{pub_prefix}/status', status_check)

    priv_prefix = f'/{app_prefix}/{api_prefix}/{ver_prefix}/{{user_id}}'

    app.router.add_post(f'{priv_prefix}/trades', trade_post)
    app.router.add_get(f'{priv_prefix}/trades', trades_get)
    app.router.add_get(f'{priv_prefix}/trades/{{trade_id}}', trade_get)
    app.router.add_put(f'{priv_prefix}/trades/{{trade_id}}', trade_put)
    app.router.add_delete(f'{priv_prefix}/trades/{{trade_id}}', trade_delete)
