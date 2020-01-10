# exchange_trade_data_api: A service that exposes an API to query data. The data is first loaded with exchange_trade_importer

## What is this

The purpose of this service is to query data.
This data comes from structured files containing cryptocurrency trades performed in exchanges.
Those files are loaded with another service: exchange_trade_importer

## Installation Guide: What do you need

The service has few dependencies:
Python
MongoDB
Poetry

## Service architecture: What, where, how and maybe why

Pending

## Database definition

MongoDB database has one schema: cryp

The schema has one collection: trades

Each trades record is composed of the following fields and the fields have the following types:

    _id: ObjectId
    strdate: String
    market: String 
    type: String [SELL, BUY]
    price: String
    amount: String
    total: String
    fee: String
    fee_coin: String
    primary_coin: Dict Object
        short_name: String
        long_name: String
    secondary_coin: Dict Object
        short_name: String
        long_name: String
    source: String
    description: String
    record_key: String
    isodate: ISODate
    meta_doc_created_at: ISODate
