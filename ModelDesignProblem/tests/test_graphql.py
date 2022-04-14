import unittest
from graphene.test import Client
from flask import current_app

from backend import create_app, db
from backend.models import Provider as ProviderModel, \
    Client as ClientModel, \
    JournalEntry as JournalModel, \
    Plan as PlanModel, \
    ClientProvider as ClientProviderModel

from backend.schema import schema
from datetime import datetime

from backend.database_init import create_database_entries


class BasicsGraphQLTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = Client(schema)

        create_database_entries(db)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        self.client = None

    def test_app_exists(self):
        assert current_app is not None

    def test_app_is_testing(self):
        assert current_app.config['TESTING']
        assert current_app.config['DEBUG']
        assert current_app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///'


class HealthieGraphQLTestCase(BasicsGraphQLTestCase):

    def test_get_clients_for_provider(self):
        executed = self.client.execute("""
                query ClientsForProvider($email: String!) {
                    providers(email:$email) {
                        name
                        clientProviders {
                        edges {
                            node {
                            client {
                                name
                                email
                            }
                            }
                        }
                        }
                    }
                    }
            """, variables={"email": "chiro@gmail.com" })

        assert executed == {"data": {
            "providers": [
                {"name": "Chiro",
                    "clientProviders": {
                    "edges": [
                        {"node": {
                            "client": {
                            "name": "Brandon",
                            "email": "bredmond1019@gmail.com"
                            }}},
                        {"node": {
                            "client": {
                            "name": "Felipe",
                            "email": "felipe@gmail.com"
                            }}},
                        {"node": {
                            "client": {
                            "name": "David",
                            "email": "david@gmail.com"
                            }
                        }
                        }
                    ]
                    }
                }
            ]}}



    def test_get_providers_for_client(self):
        executed = self.client.execute("""
                query ProvidersForClient($email: String!) {
                    clients(email:$email) {
                        name
                        clientProviders {
                        edges {
                            node {
                            provider {
                                name
                            }
                            plan {
                                planType
                            }
                            }
                        }
                        }
                    }
                    }
            """, variables={"email": "bredmond1019@gmail.com" })
        
        assert executed == {"data": {
           "clients": [
                {"name": "Brandon",
                "clientProviders": {
                "edges": [
                        {"node": {
                            "provider": {"name": "Chiro"},
                            "plan": {"planType": "BASIC"}
                        }},
                        {"node": {
                            "provider": {"name": "Physical Therapist"},
                            "plan": {"planType": "BASIC"}
                        }},
                        {
                        "node": {
                            "provider": {"name": "Doctor"},
                            "plan": {"planType": "BASIC"}
                        }}]}}]}}


    def test_get_journals_for_client(self):
        executed = self.client.execute("""
                query JournalsForClient($email: String!) {
                    clients(email:$email) {
                        name
                        journalEntries {
                        entry
                        clientId
                        }
                    }
                    }
            """, variables={"email": "bredmond1019@gmail.com" })
        
        test_case = {"data": {
            "clients": [
                {"name": "Brandon",
                "journalEntries": [
                    {"entry": "Brandon loves Healthie!","clientId": 1,},
                    {"entry": "Brandon loves to rock climb","clientId": 1,}
                    ]}]}}

        assert test_case == executed


    def test_get_all_journals_all_clients_for_provider(self):
        executed = self.client.execute("""
                query JournalsForClient($email: String!) {
                    providers(email:$email) {
                        name
                        clientProviders {
                        edges {
                            node {
                            client {
                                name
                                email
                                journalEntries {
                                entry 
                                }
                            }
                            }
                        }
                        }
                    }
                    }
                """, variables={"email": "chiro@gmail.com" })


        assert executed == {"data": {
                    "providers": [
                {"name": "Chiro",
                "clientProviders": {
                "edges": [
                    {"node": {
                        "client": {
                            "name": "Brandon",
                            "email": "bredmond1019@gmail.com",
                            "journalEntries": [
                                {"entry": "Brandon loves Healthie!",},
                                {"entry": "Brandon loves to rock climb",}
                            ]}}},
                    {"node": {
                        "client": {
                            "name": "Felipe",
                            "email": "felipe@gmail.com",
                            "journalEntries": [
                                {"entry": "Felipe loves Brazil!",}
                            ]}}},
                    {"node": {
                        "client": {
                            "name": "David",
                            "email": "david@gmail.com",
                            "journalEntries": [
                                {"entry": "David loves code!",}
                            ]}}}]}}]}}