import graphene
from datetime import date

from backend import db
from ..models import Provider as ProviderModel, \
    Client as ClientModel, \
    JournalEntry as JournalModel, \
    Plan as PlanModel, \
    ClientProvider as ClientProviderModel

from ..graphql.objects import ProviderObject, ClientObject, JournalObject, ClientProviderObject

# Provider Mutation
class ProviderMutation(graphene.Mutation):
    class Arguments: 
        name = graphene.String(required=True)
        email = graphene.String(required=True)

    provider = graphene.Field(lambda: ProviderObject)

    def mutate(self, info, name, email):
        provider = ProviderModel(name=name, email=email)

        db.session.add(provider)
        db.session.commit()

        return ProviderMutation(provider=provider)


# Client Mutation
class ClientMutation(graphene.Mutation):
    class Arguments: 
        name = graphene.String(required=True)
        email = graphene.String(required=True)

    client = graphene.Field(lambda: ClientObject)

    def mutate(self, info, name, email):
        client = ClientModel(name=name, email=email)

        db.session.add(client)
        db.session.commit()

        return ClientMutation(client=client)

# Journal Mutation
class JournalMutation(graphene.Mutation):
    class Arguments: 
        entry = graphene.String(required=True)
        client_id = graphene.Int(required=True)

    journal = graphene.Field(lambda: JournalObject)

    def mutate(self, info, entry, client_id):
        journal = JournalModel(entry=entry, client_id=client_id)

        db.session.add(journal)
        db.session.commit()

        return JournalMutation(journal=journal)

# Client | Provider | Plan Association Table Mutation
class ClientProviderMutation(graphene.Mutation):
    class Arguments: 
        client_id = graphene.Int(required=True)
        provider_id = graphene.Int(required=True)
        plan_id = graphene.Int()

    client_provider = graphene.Field(lambda: ClientProviderObject)

    def mutate(self, info, client_id, provider_id, plan_id = 1):
        client_provider = ClientProviderModel(client_id=client_id, provider_id=provider_id, plan_id=plan_id)

        db.session.add(client_provider)
        db.session.commit()

        return ClientProviderMutation(client_provider=client_provider)





# All Mutations sent to Schema
class Mutation(graphene.ObjectType):
    mutate_provider = ProviderMutation.Field()
    mutate_client = ClientMutation.Field()
    mutate_journal = JournalMutation.Field()
    mutate_client_provider = ClientProviderMutation.Field()


