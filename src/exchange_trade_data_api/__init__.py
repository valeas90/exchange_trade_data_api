
from argparse import ArgumentParser
from configparser import ConfigParser
from pathlib import Path
import sys
import os

from .models import setup_databases
from .routes import setup_routes

import aiohttp
from aiohttp.web import Application
import aiohttp.web


def get_args():
    parser = ArgumentParser(description="exchange_trade_data_api")
    parser.add_argument(
        '-p', '--prefix', default='etda', help='URI base prefix')
    parser.add_argument(
        '-P', '--port', default=8080, type=int, help='Port to listen on')
    parser.add_argument(
        '-H',
        '--host',
        default='127.0.0.1',
        type=str,
        help='Host name of the server')
    parser.add_argument(
        '-c',
        '--config',
        default='./etc/config.ini',
        type=Path,
        help='Config file path')
    parser.add_argument(
        '-l', '--logs', type=Path, help='Path to store logs to')
    parser.add_argument(
        '-d', '--debug', action='store_true', help='Enable debug mode')

    return parser.parse_args(sys.argv[1:])


def get_app(args):
    """Extract aiohttp application with default configuration.

    This sets up routes, databases, config and logging.
    Can be used alongside wsgi or gunicorn safely.
    """
    app = Application(middlewares=[], debug=args.debug)

    app['config'] = ConfigParser()
    app['config'].read(str(args.config))

    # Setup routes and databases
    app.on_startup.append(setup_databases)
    setup_routes(app, args.debug, args.prefix)

    return app


def main():
    args = get_args()
    app = get_app(args)
    aiohttp.web.run_app(app, host=args.host, port=args.port)
