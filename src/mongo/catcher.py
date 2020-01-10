#!/usr/bin/python
# -*- coding: utf-8 -*-
from pymongo.errors import PyMongoError
from pymongo.errors import ConnectionFailure
from pymongo.errors import OperationFailure

from bson.errors import InvalidId


def catcher(method):
    async def wrapper(self, *args, **kwargs):
        result = error = None

        try:
            result = await method(self, *args, **kwargs)

        except ConnectionFailure as exception:
            error = {
                'category': 'connection',
                'error': 'connection_lost',
                'exception': exception,
                'message': str(exception)
            }

        except OperationFailure as exception:
            error = {
                'category': 'operation',
                'error': 'operation_failed',
                'exception': exception,
                'message': str(exception)
            }

        except PyMongoError as exception:
            error = {
                'category': 'mongo',
                'error': 'unknow',
                'exception': exception,
                'message': str(exception)
            }

        except InvalidId as exception:
            error = {
                'category': 'mongo',
                'error': 'invalid_id',
                'exception': exception,
                'message': str(exception)
            }

        except Exception as exception:
            error = {
                'category': 'undefined',
                'error': 'unknow',
                'message': str(exception),
                'exception': exception
            }

        finally:
            return result, error

    return wrapper
