#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 13:38:04 2018

@author: agile
"""

from flask import Flask, Response
from flask_restful import Api, Resource, reqparse
from classification_v2 import label_address
import os
import json

app = Flask(__name__)
api = Api(app)

class User(Resource):
    def get(self, address):
        address = str(address).split(',')
        final_labels = ''
        final_labels = label_address(address)
        if len(final_labels) != 0:
            resp = Response(response=final_labels.to_json(), status=200, mimetype="application/json")
            return (resp)
        return ("Not founds", 404)

class instruct(Resource):
    def get(self):
        return('Usage: https://bitcoin-wallet-classifier.herokuapp.com/wallet-addresses OR https://bitcoin-wallet-classifier.herokuapp.com/address1,address2...')
        
api.add_resource(User, "/<string:address>")
api.add_resource(instruct, "/")

port = int(os.environ.get("PORT", 4000))
app.run(debug=False, port=port, host='0.0.0.0')

