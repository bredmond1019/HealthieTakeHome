from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView
from config import config

from .database_init import create_database_entries


db = SQLAlchemy()


# Flask Application Factory
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config.from_pyfile("../config.py")

    db.init_app(app)


    # If you are just using the sqlite database I provided, leave this alone
    # Otherwise comment this if statement out after the PostgreSQL database is initilized
    if config_name == 'development':
        @app.before_first_request
        def initialize_database():
            create_database_entries(db)
        
    # Connect Flask to GraphQL
    from .schema import schema

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True
        )
    )

    # Register the API Blueprint to the current app
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app
