from exchange_trade_data_api.models.trades import Trades
from exchange_trade_data_api import utils as etda_utils
from aiohttp.web import json_response
import datetime
import uuid


VISIBLE_FIELDS = {
    "trade_uuid", "strdate", "market", "type", "price", "amount", "total",
    "fee", "fee_coin", "primary_coin", "secondary_coin", "source",
    "description", "meta_record_key", "meta_doc_created_at", "traded_at"
}

async def trade_get(request):
    path_params = dict(request.match_info)
    user_id = path_params.get('user_id')
    trade_uuid = path_params.get('trade_id')
    
    kwargs = {
        'filter': {'trade_uuid': trade_uuid, 'user_id': user_id},
        'skip': 0,
        'limit': 1
    }

    trades = Trades(request.app)
    result, err = await trades.find(**kwargs)

    if err:
        return json_response({'status': 400, 'detail': 'database_error'})
    else:
        v_result = []
        for record in result:
            v_record = dict(
                [(e, v) for e, v in record.items() if e in VISIBLE_FIELDS])
            v_result.append(v_record)
        v_result = [] if not v_result else v_result[0]
        if not v_result:
            return json_response({'status': 404})
        else:
            return json_response({'status': 200, 'payload': v_result})


async def trades_get(request):
    path_params = dict(request.match_info)
    user_id = path_params.get('user_id')

    query_params = dict(request.query)
    kwargs = {
        'filter': {'user_id': user_id},
        'skip': int(query_params.get('skip', '0')),
        'limit': int(query_params.get('limit', '10'))
    }

    trades = Trades(request.app)
    result, err = await trades.find(**kwargs)

    if err:
        return json_response({'status': 400, 'detail': 'database_error'})
    else:
        v_result = []
        for record in result:
            v_record = dict(
                [(e, v) for e, v in record.items() if e in VISIBLE_FIELDS])
            v_result.append(v_record)

        return json_response({'status': 200, 'payload': v_result})


async def trade_delete(request):
    response = {'status': 400, 'detail': 'not_implemented'}
    return json_response(response)


async def trade_post(request):
    response = {'status': 400, 'detail': 'not_implemented'}
    return json_response(response)


async def trade_put(request):
    response = {'status': 400, 'detail': 'not_implemented'}
    return json_response(response)
