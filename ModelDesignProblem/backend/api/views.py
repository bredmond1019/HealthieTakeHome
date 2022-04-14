from flask import render_template, Response, jsonify, request
from . import api
from ..models import Provider, Client, Plan, ClientProvider, JournalEntry
from backend import db
from datetime import datetime


# Here is the start of an API blueprint
# We can add REST API endpoints here as needed
# For now, all of the queries and mutations
# Are done through GraphQL



# Will list out all of the Client-Provider-Plan Association Table
@api.route('/')
def index():
    client_providers = ClientProvider.query.all()

    data = [client_provider.to_dict() for client_provider in client_providers ]

    return jsonify({"client_providers": data}), {'Content-Type': 'application/json'}
    

