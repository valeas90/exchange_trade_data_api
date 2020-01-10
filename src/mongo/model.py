#!/usr/bin/python
# -*- coding: utf-8 -*-
from bson import ObjectId
from datetime import datetime

from pymongo import ReturnDocument

from mongo.catcher import catcher


class Model(object):
    def __init__(self, app):
        self.application = app

        self.database = self.application['mongo_db']

    @property
    def collection(self):
        return self.database[self.__class__.__name__.lower()]

    @catcher
    async def save(self, data, query=None, upsert=True):
        result = await self.collection.find_one_and_update(**{
            'filter': query or {},
            'update': data,
            'upsert': upsert,
            'return_document': ReturnDocument.AFTER
        })

        return Model.normalize(result)

    @catcher
    async def insert(self, data):
        result = await self.collection.insert_one(data)

        if not result:
            return

        data['_id'] = result.inserted_id

        return Model.normalize(data)

    @catcher
    async def one(self, **kwargs):
        result = await self.collection.find_one(**{
            'projection': kwargs.pop('fields', None),
            'filter': kwargs
        })
        return Model.normalize(result)

    @catcher
    async def get(self, document_id, fields=None):
        result = await self.collection.find_one(**{
            'projection': fields,
            'filter': {'_id': ObjectId(document_id)}
        })
        return Model.normalize(result)

    @catcher
    async def pop(self, document_id):
        result = await self.collection.delete_one(filter={
            '_id': ObjectId(document_id)
        })
        return result.deleted_count == 1

    @catcher
    async def find(self, **kwargs):
        items = await self.collection.find(**kwargs).to_list(None)
        return Model.normalize(items)

    @catcher
    async def count(self, filter: dict, **kwargs):
        """Count all documents in a collectio.

        Note: The original documentation can be found in
        https://motor.readthedocs.io/en/stable/api-tornado/motor_collection.html#motor.motor_tornado.MotorCollection.count

        Args:
            filter: Fields and values with which the query will be filtered.

        Returns:
            An integer indicating the total number of documents belongs
            to the collection.
        """
        if '_id' in filter:
            filter['_id'] = ObjectId(filter['_id'])
        return await self.collection.count_documents(filter, **kwargs)

    @staticmethod
    def normalize(value):
        if isinstance(value, list):
            return [Model.normalize(field) for field in value]

        elif isinstance(value, dict):
            return {field: Model.normalize(value[field]) for field in value}

        elif isinstance(value, datetime):
            return value.strftime('%Y-%m-%d %H:%M:%S')

        elif isinstance(value, ObjectId):
            return str(value)

        return value
